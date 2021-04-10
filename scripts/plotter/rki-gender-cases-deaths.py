"""
NOTE: This code is part of CDP (Corona-Data-Proejct) developed by @masdot. 
Copyright (c) 2021 masdot - Licensed under MIT License (https://github.com/masdot/cdp-corona-data-project/blob/main/LICENSE)
---


This file uses the current data CSV from the RKI to plot infection and death cases by gender.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Remove max from cols + row for large dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Download newest CSV file with RKI data
RKIData = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv');

# Save 'Datenstand' of last entry
last_row = RKIData.iloc[-1]
last_datenstand = last_row['Datenstand']

# Remove empty entries
RKIData = RKIData[RKIData.Geschlecht.str.contains("unbekannt") == False]
RKIData = RKIData[RKIData.Altersgruppe.str.contains("unbekannt") == False]

# Clean dataframe
frame = RKIData.drop(['NeuGenesen', 'AnzahlGenesen', 'IstErkrankungsbeginn', 'ObjectId', 'IdBundesland', 'IdLandkreis', 'NeuerFall', 'NeuerTodesfall'],axis=1)
frame = frame.groupby(['Geschlecht']).sum()

# Plot dataframe
fig, axs = plt.subplots
axs[0].plot(kind="bar",figsize=(20,10),secondary_y="AnzahlTodesfall",title='Infektionen und Todesfälle nach Geschlecht').ticklabel_format(axis="y", style="plain")
# plots = frame.plot(kind="bar",figsize=(20,10),secondary_y="AnzahlTodesfall",title='Infektionen und Todesfälle nach Geschlecht')

fig, axs = plt.subplots(2, 2)

# Save file
plt.savefig(os.path.join('plots/rki','gender-cases-deaths.png'),dpi=300,pad_inches=5)