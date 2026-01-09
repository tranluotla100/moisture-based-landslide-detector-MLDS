# Moisture-Based Landslide Detection System

This project implements a physically-based landslide detection model using
satellite rainfall and terrain data.

## Data Sources
- SRTM Digital Elevation Model (30 m resolution)
- NASA GPM IMERG Hourly Precipitation

## Methodology
1. Compute slope from DEM
2. Estimate soil moisture from rainfall using an infiltration model
3. Compute Factor of Safety using an infinite slope stability model
4. Identify landslide failure and warning zones

## Requirements
- Python 3.10+
- numpy
- rasterio
- xarray
- netCDF4
- matplotlib

## Output
- Factor of Safety (FS)
- Landslide failure and warning pixels

## Disclaimer
This is a simplified research/educational model and not an operational
early warning system.
