# data merging

import csv
import pandas as pd

data1 = [] #array from the dataset_2.csv
planet_data = []

with open("main.csv","r") as f: #opening main.csv and reading/appending each row to data1 array
    csvreader = csv.reader(f) 
    for row in csvreader: 
        data1.append(row)

header_1 = data1[0] #the headers from the first row
planet_data_1 = data1[1:] #the data from row 2 onwards

mass = []
for planet_data in planet_data_1[3]:
    mass_value = float(planet_data)*0.000954588
    mass.append(mass_value)

radius = []
for planet_data in planet_data_1[7]:
    radius_value = float(planet_data)*0.102763
    radius.append(radius_value)

mass_radius = mass+radius

with open ("final.csv","a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(mass_radius) 
    csvwriter.writerows(planet_data) 
