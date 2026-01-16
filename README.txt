Overview

This project is a proof of concept implementing a first-order, physically based landslide susceptibility model using digital elevation data (DEM) and rainfall input. Terrain slope, soil moisture increase, and an infinite slope stability model are combined to compute a spatial Factor of Safety (FS) identifying potentially unstable slopes.

The model is designed for conceptual understanding and rapid screening, not for calibrated prediction.

Model Summary

Slope derived from DEM

Rainfall forcing from gridded data

Simplified soil-moisture bucket model

Infinite slope stability formulation

Instability thresholds: FS < 1.0 (failure), FS < 1.3 (warning)

Caveats

Rainfall is spatially averaged

Soil properties are uniform

No temporal evolution of infiltration

Pore pressure is parameterized

No hydrological routing or calibration

Outputs are qualitative and should not be interpreted as real-world hazard predictions.
