"""
NOTE: This code is part of CDP (Corona-Data-Proejct) developed by @masdot. 
Copyright (c) 2021 masdot - Licensed under MIT License (https://github.com/masdot/cdp-corona-data-project/blob/main/LICENSE)
---


This file uses the current data CSV from the RKI to plot infection and death cases by age.
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
frame_pre = RKIData.drop(['NeuGenesen', 'AnzahlGenesen', 'IstErkrankungsbeginn'],axis=1)
frame = frame_pre.groupby(['Altersgruppe']).sum().reset_index()

# Plot dataframe
plt.subplots(figsize=(8,10))
ax = plt.subplot(111)
ax.plot(frame['Altersgruppe'], frame['AnzahlTodesfall'])
ax.set_xlabel("Altersgruppe",fontsize=14)
ax.set_ylabel("Anzahl Todesfälle",fontsize=14,color='C0')

ax2=ax.twinx()
ax2.plot(frame['Altersgruppe'], frame['AnzahlFall'], color='C1')
ax2.set_ylabel("Anzahl Fälle",fontsize=14,color='C1')
ax2.ticklabel_format(axis="y", style="plain")
ax.set(xlim=(0), ylim=(0))

plt.title('Infektionen und Todesfälle nach Altersgruppen', size=14)
plt.text(0.5,-0.12, f"Datenquelle: Robert-Koch-Institut(Datenstand {last_datenstand})", size=12, ha="center", transform=ax2.transAxes)

# Save file
plt.savefig(os.path.join('plots/rki','age_group-cases-deaths.png'),dpi=200,pad_inches=5)
