import pandas as pd
import numpy as np
import os

# Finding Stellar Spectral type Using Effective Temperatures
def assign_spec_type_use_t_eff(t_eff):
    star_type = ""
    if t_eff < 3700:
        star_type = "M"
    elif 3700 <= t_eff < 5200:
        star_type = "K"
    elif 5200 <= t_eff < 6000:
        star_type = "G"
    elif 6000 <= t_eff < 7500:
        star_type = "F"
    elif 7500 <= t_eff < 10000:
        star_type = "A"
    elif 10000 <= t_eff:
        star_type = "B"
    
    return star_type

# Using Stellar Masses to Find Stellar Spectral type
def assign_spec_type_use_mass(star_mass):
    star_type = ""
    if star_mass < 0.45:
        star_type = "M"
    elif 0.45 <= star_mass < 0.8:
        star_type = "K"
    elif 0.8 <= star_mass < 1.04:
        star_type = "G"
    elif 1.04 <= star_mass < 1.4:
        star_type = "F"
    elif 1.4 <= star_mass < 2.1:
        star_type = "A"
    elif 2.1 <= star_mass:
        star_type = "B"
    
    return star_type

# Finding the stellar effective temperature using Spectral type
def assign_t_eff_use_spec_type(spec_type):
    t_eff = 0
    if spec_type == "M":
        t_eff = 3000
    elif spec_type == "K":
        t_eff = 4400
    elif spec_type == "G":
        t_eff = 5600
    elif spec_type == "F":
        t_eff = 6700
    elif spec_type == "A":
        t_eff = 8700
    elif spec_type == "B":
        t_eff = 20000
    
    return t_eff

# Using stellar mass to find the stellar effective temperature
def assign_t_eff_use_mass(star_mass):
    t_eff = 0
    if star_mass < 0.45:
        t_eff = 3000
    elif 0.45 <= star_mass < 0.8:
        t_eff = 4400
    elif 0.8 <= star_mass < 1.04:
        t_eff = 5600
    elif 1.04 <= star_mass < 1.4:
        t_eff = 6700
    elif 1.4 <= star_mass < 2.1:
        t_eff = 8700
    elif 2.1 <= star_mass:
        t_eff = 20000
    
    return t_eff

# Using Stellar Spectral type to Find Stellar Masses
def assign_mass_use_spec_type(spec_type):
    star_mass = 0
    if spec_type == "M":
        star_mass = 0.26
    elif spec_type == "K":
        star_mass = 0.62
    elif spec_type == "G":
        star_mass = 0.92
    elif spec_type == "F":
        star_mass = 1.22
    elif spec_type == "A":
        star_mass = 1.75
    elif spec_type == "B":
        star_mass = 9
    
    return star_mass

# Finding the stellar mass using the stellar effective temperature
def assign_mass_use_t_eff(t_eff):
    star_mass = 0
    if t_eff < 3700:
        star_mass = 0.26
    elif 3700 <= t_eff < 5200:
        star_mass = 0.62
    elif 5200 <= t_eff < 6000:
        star_mass = 0.92
    elif 6000 <= t_eff < 7500:
        star_mass = 1.22
    elif 7500 <= t_eff < 10000:
        star_mass = 1.75
    elif 10000 <= t_eff:
        star_mass = 9
    
    return star_mass

# Using Planetary Orbital Periods to Find a Planet semi-major axis
def assign_semi_major_use_period(period):
    semi_major = period ** (2/3)
    
    return semi_major

# Using Planet semi-major axis to Find Planetary Orbital Periods
def assign_period_use_semi_major(semi_major):
    period = semi_major ** (3/2)
    
    return period

# Using Stellar Mass to Find Stellar Luminosity
def assign_luminosity_use_mass(star_mass):
    luminosity = 0
    if star_mass < 0.45:
        luminosity = 0.045
        luminosity = np.log10(luminosity)
    elif 0.45 <= star_mass < 0.8:
        luminosity = 0.34
        luminosity = np.log10(luminosity)
    elif 0.8 <= star_mass < 1.04:
        luminosity = 1.05
        luminosity = np.log10(luminosity)
    elif 1.04 <= star_mass < 1.4:
        luminosity = 3.25
        luminosity = np.log10(luminosity)
    elif 1.4 <= star_mass < 2.1:
        luminosity = 15
        luminosity = np.log10(luminosity)
    elif 2.1 <= star_mass:
        luminosity = 15000
        luminosity = np.log10(luminosity)
    
    return luminosity

# Finding stellar radius using stellar luminosity and effective temperature
def assign_radius_use_t_eff_and_luminosity(t_eff, luminosity):
    radius = 0
    if t_eff >0 :
        star_luminosity = 3.828*10**(26) * 10**(luminosity)
        radius = 1/(4*np.pi*5.67*10**(-8)) * star_luminosity / t_eff**4
        radius = np.sqrt(radius) / (696340*1000)
        
    return radius

# Using planet radius and mass to find planet density
def assign_density_use_radius_and_mass(planet_mass, planet_radius):
    density = 0
    if planet_mass > 0 and planet_radius > 0:
        density = planet_mass * 5.972 * 10**27 / (4/3 * np.pi * 6371 * 10**5 * planet_radius**3)
    if density <=0:
        density = None
        
    return density

# Using stellar spectral type, luminosity, and apparent magnitude to find Earth-planet system distances
def assign_dist_use(spec_type, luminosity, magnitude):
    distance = 0
    if spec_type!= None :
        absolute_magnitude_bol = -2.5 * luminosity + 4.74
        BC = 0
        if spec_type =="B" : BC = -2.0
        if spec_type =="A" : BC = -0.3
        if spec_type =="F" : BC = -0.15
        if spec_type =="G" : BC = -0.4
        if spec_type =="K" : BC = -0.8
        if spec_type =="M" : BC = -2.0
        
        if BC !=0 :     
            absolute_magnitude = absolute_magnitude_bol - BC
            distance = 10**((magnitude - absolute_magnitude) / 5 ) * 10
        
        return distance

# Using stellar spectral type and Earth-planetary system distance to find stellar apparent magnitude
def assign_mag_use_spec_type_and_dist(spec_type, distance):
    magnitude = 0
    if spec_type!= None :
        absolute_magnitude = 0
        if spec_type =="B" : absolute_magnitude = -3.5
        if spec_type =="A" : absolute_magnitude = 1.25
        if spec_type =="F" : absolute_magnitude = 3.25
        if spec_type =="G" : absolute_magnitude = 5
        if spec_type =="K" : absolute_magnitude = 7
        if spec_type =="M" : absolute_magnitude = 11
        
        if absolute_magnitude !=0 :     
            magnitude = absolute_magnitude + 5 * np.log(distance / 10)
            
        return magnitude

# fill in null values in an array containing null values >> return a filled array
def none_to_value(array, none_indices, column_name):
    
    # return how many nulls are in a row
    number = len(none_indices)  
    
    # Traversing null value indices one by one to assign exact values
    for i in range(number): 
        
        # Return a flag corresponding to the index of a null value in a predefined column name 
        none_flag = column_name[none_indices[i]]
        
        # Use the appropriate function for each flag when it has a null value
        if none_flag == "st_spectype" : 
            if array[16] == None and not np.isnan(array[14]):
                array[none_indices[i]] = assign_spec_type_use_t_eff(array[14])
            elif np.isnan(array[14]) and array[16] != None:
                array[none_indices[i]] = assign_spec_type_use_mass(array[16])
            elif not np.isnan(array[14]) and array[16] != None:
                array[none_indices[i]] = assign_spec_type_use_t_eff(array[14])
                    
        if none_flag == "st_teff" : 
            if array[16] == None and array[13] != None:
                array[none_indices[i]] = assign_t_eff_use_spec_type(array[13][0])
            elif array[13] == None and array[16] != None:
                array[none_indices[i]] = assign_t_eff_use_mass(array[16])
            elif array[13] != None and array[16] != None:
                array[none_indices[i]] = assign_t_eff_use_mass(array[16])
                
        if none_flag == "st_mass" : 
            if array[14] == None and array[13] != None:
                array[none_indices[i]] = assign_mass_use_spec_type(array[13][0])
            elif array[13] == None and array[14] != None:
                array[none_indices[i]] = assign_mass_use_t_eff(array[14])
            elif array[13] != None and array[14] != None:
                array[none_indices[i]] = assign_mass_use_t_eff(array[14])
        
        if none_flag == "pl_orbper" : 
            if array[7] != None :
                array[none_indices[i]] = assign_period_use_semi_major(array[7])
                
        if none_flag == "pl_orbsmax" : 
            if array[6] != None :
                array[none_indices[i]] = assign_semi_major_use_period(array[6])
                
        if none_flag == "st_lum" : 
            if array[16] != None :
                array[none_indices[i]] = assign_luminosity_use_mass(array[16])
        
        if none_flag == "st_rad" : 
            if np.isnan(array[17]) :
                array[17] = assign_luminosity_use_mass(array[16])
            if not np.isnan(array[14]) :
                array[none_indices[i]] = assign_radius_use_t_eff_and_luminosity(array[14], array[17])
        
        if none_flag == "pl_dens" : 
            if array[8] != None and array[9] != None:
                array[none_indices[i]] = assign_density_use_radius_and_mass(array[8], array[9])
                
        if none_flag == "sy_dist" : 
            if array[13] != None and array[17] != None and array[24] != None:
                array[none_indices[i]] = assign_dist_use(array[13], array[17], array[24])
                
        if none_flag == "sy_vmag" : 
            if array[13] != None and array[23] != None and array[23] != 0:
                array[none_indices[i]] = assign_mag_use_spec_type_and_dist(array[13], array[23])
            if array[23] == None :
                array[23] = assign_dist_use(array[13], array[17], array[24])
            
    return array

# Specify the path to the source CSV file: file_path="./your_csv_path"
file_path = "C:/Users/kjun1/Desktop/NASA/NASA_important_data.csv"  
df = pd.read_csv(file_path, comment='#')

# Determine the total number of exoplanets
number_of_row = df.shape[0]

# Define each column name
column_name = ["pl_name", "hostname", "discoverymethod", "disc_year", "disc_facility", "disc_telescope", "pl_orbper",   
               "pl_orbsmax", "pl_rade", "pl_bmasse", "pl_dens", "pl_orbeccen", "pl_orbincl", "st_spectype", "st_teff",   
               "st_rad", "st_mass", "st_lum", "st_dens", "rastr", "ra", "decstr", "dec", "sy_dist", "sy_vmag"]

# Declare a two-dimensional array to store the modified array
total_array = []

# Filling in null values for each row in the CSV file
for row_index in range(number_of_row):
    
    # Get data for a specific row and convert to an array
    row = df.iloc[row_index]
    array = row.to_numpy()

    # Return a list of indices in the converted numpy array that are null values
    none_indices = np.where(pd.isna(array))[0]  
    
    # Fill in the indexes with null values and store the array in a full two-dimensional array
    filled_array = none_to_value(array, none_indices, column_name)
    total_array.append(filled_array)
  
total_array = np.array(total_array)

# Specifying the output file path and writing the array data to a CSV file
new_df = pd.DataFrame(total_array)
new_file_path = "C:/Users/kjun1/Desktop/NASA/NASA_important_data_filled.csv"  

# If there are any files in the output path, delete and regenerate them
if os.path.exists(new_file_path):
    os.remove(new_file_path)
    
new_df.to_csv(new_file_path, index=False, header=False)  