import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# Remove max from cols + row for large dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Download newest CSV file with RKI data
RKIData = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv')

# Save 'Datenstand' of last entry
last_row = RKIData.iloc[-1]
last_datenstand = last_row['Datenstand']

# Remove empty entries
RKIData = RKIData[RKIData.Geschlecht.str.contains("unbekannt") == False]
RKIData = RKIData[RKIData.Altersgruppe.str.contains("unbekannt") == False]

# Clean dataframe
frame_pre = RKIData.drop(['NeuGenesen', 'AnzahlGenesen', 'IstErkrankungsbeginn'],axis=1)

frame_pre.head()