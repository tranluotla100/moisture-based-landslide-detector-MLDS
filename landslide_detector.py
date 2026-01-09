import rasterio
import numpy as np

with rasterio.open("dem.tif") as src:
    elev = src.read(1).astype(float)

dx, dy = np.gradient(elev)
slope = np.arctan(np.sqrt(dx**2 + dy**2))

print("DEM loaded successfully")
print("Elevation shape:", elev.shape)
print("Slope shape:", slope.shape)
print("Max slope (deg):", np.degrees(slope).max())

import xarray as xr

ds = xr.open_dataset(
    "rain.hdf5",
    engine="netcdf4",
    group="Grid"
)

print("Rainfall dataset opened")
print(ds)

rain = ds["precipitation"].isel(time=0)

print("Rainfall extracted")
print("Rain shape:", rain.shape)
print("Max rainfall (mm/hr):", float(rain.max()))

# ---- Soil moisture bucket model ----

# Convert rainfall to meters
P_mean = float(rain.mean()) / 1000.0  # m/hr

# Soil parameters
Z = 1.0          # effective soil depth (m)
theta0 = 0.15    # initial moisture
theta_sat = 0.45 # saturation moisture

# Uniform moisture increase (fast prototype)
theta = theta0 + P_mean / Z
theta = np.clip(theta, 0, theta_sat)

# Expand to DEM shape
theta_map = np.full(elev.shape, theta)

print("Soil moisture computed")
print("Mean soil moisture:", theta)

# ---- Infinite slope stability model ----

# Physical parameters (reasonable defaults)
rho = 2000        # soil bulk density (kg/m^3)
g = 9.81
c = 5000          # cohesion (Pa)
phi = np.deg2rad(30)  # friction angle
alpha = 10000     # moisture -> pore pressure scaling

# Pore water pressure from moisture
u = alpha * (theta_map / theta_sat)

# Factor of Safety
FS = (c + (rho * g * Z * np.cos(slope)**2 - u) * np.tan(phi)) / \
     (rho * g * Z * np.sin(slope) * np.cos(slope) + 1e-6)

# Landslide risk
failure = FS < 1.0
warning = FS < 1.3

print("Min FS:", FS.min())
print("Failing pixels:", failure.sum())
print("Warning pixels:", warning.sum())
