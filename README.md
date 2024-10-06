# Exoplanet Data Analysis and Processing

## Overview
This project involves analyzing and processing exoplanet data, focusing on filling missing values using astronomical principles and custom functions. The code performs operations to find missing values and populate them based on relationships between various stellar and planetary attributes, such as effective temperature, stellar mass, and luminosity.

## Features
- **Stellar Spectral Type Calculation**: Determines the stellar spectral type using effective temperature or stellar mass.
- **Effective Temperature and Mass Calculation**: Calculates stellar effective temperature based on the spectral type or mass.
- **Planetary and Stellar Attribute Estimations**: Estimates attributes like semi-major axis, orbital period, luminosity, radius, and density.
- **Handling Missing Data**: Fills missing values using interdependent calculations between different features of planets and stars.

## Data
The code uses data from the `NASA_filtered_imaging.csv` file, which includes various planetary and stellar attributes:

- `pl_name`: Planet name
- `st_teff`: Stellar effective temperature
- `st_mass`: Stellar mass
- `st_lum`: Stellar luminosity
- `pl_orbper`: Orbital period
- `pl_orbsmax`: Semi-major axis of the orbit
- And many other attributes relevant for analyzing planetary systems.

## How It Works
1. **Load and Process CSV File**: The code loads the exoplanet dataset CSV file using pandas and determines the number of rows.
2. **Identify Missing Values**: For each row, the code checks for missing values and determines the column names that contain them.
3. **Fill Missing Values**: The function `none_to_value` is called to fill the missing values using predefined logic and astronomical calculations, such as:
    - Finding stellar spectral type using stellar mass or effective temperature.
    - Estimating stellar mass based on spectral type.
    - Calculating luminosity using stellar mass.
4. **Save to New CSV File**: After filling all the missing values, the new dataset is saved to a CSV file for further analysis.

## Key Functions

- `assign_spec_type_use_t_eff(t_eff)`: Assigns a spectral type based on the given effective temperature.
- `assign_spec_type_use_mass(star_mass)`: Assigns a spectral type based on the given stellar mass.
- `assign_t_eff_use_spec_type(spec_type)`: Determines effective temperature based on the spectral type.
- `assign_mass_use_spec_type(spec_type)`: Determines stellar mass based on the spectral type.
- `assign_luminosity_use_mass(star_mass)`: Calculates stellar luminosity based on stellar mass.
- `assign_density_use_radius_and_mass(planet_mass, planet_radius)`: Calculates planetary density using radius and mass.
- `none_to_value(array, none_indices, column_name)`: Fills missing values in an array by determining the relationship between different astronomical attributes.

## How to Run
1. **Set Up the Environment**: Ensure you have Python installed along with the necessary libraries (`pandas`, `numpy`, `os`).
2. **Prepare the Data**: Place the CSV file (`NASA_filtered_imaging.csv`) in the specified path.
3. **Run the Script**: Execute the Python script to fill in missing values and generate a new CSV file with the processed data.
    ```bash
    python habitable_calculator.py
    ```
4. **Output**: The processed data will be saved in a new file called `NASA_important_data_filled.csv`.

## Project Structure

