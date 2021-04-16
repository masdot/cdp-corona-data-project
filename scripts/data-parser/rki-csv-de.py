"""
This file uses the current data CSV (^1) from RKI to save it as new cleaned csv.
^1: RKI data via CSV (daily updated) - https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0

"""

import pandas as pd
import os
from datetime import date

# Disable dataframe max for big dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def main():
  # url = 'https://www.arcgis.com/sharing/rest/content/items/f10774f1c63e40168479a1feb6c7ca74/data'

  # Read last RKI CSV
  RKIData = pd.read_csv(
      'https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv',
      parse_dates=True
  )

  # Clean df: remove cols
  RKIData = RKIData.drop(["Altersgruppe2","ObjectId","IdBundesland","Bundesland","Landkreis","Altersgruppe","Geschlecht","IdLandkreis","Datenstand","NeuerFall","NeuerTodesfall","NeuGenesen","IstErkrankungsbeginn"],axis=1)

  # Create df: cases, deaths, recoverd by 'Meldedatum'
  RKIData_cdr_by_melde = RKIData.drop(["Refdatum"],axis=1)
  # Clean df
  RKIData_cdr_by_melde_clean = RKIData_cdr_by_melde.groupby('Meldedatum').sum().reset_index()
  RKIData_cdr_by_melde_clean= RKIData_cdr_by_melde_clean.head(900)
  RKIData_cdr_by_melde_clean.sum().reset_index()
  RKIData_cdr_by_melde = RKIData_cdr_by_melde_clean

  # Create df: cases, deaths, recoverd by 'Refdatum'
  RKIData_cdr_by_ref = RKIData.drop(["Meldedatum"],axis=1)
  # Clean df
  RKIData_cdr_by_ref_clean = RKIData_cdr_by_ref.groupby('Refdatum').sum().reset_index()
  RKIData_cdr_by_ref_clean= RKIData_cdr_by_ref_clean.head(900)
  RKIData_cdr_by_ref_clean.sum().reset_index()
  RKIData_cdr_by_ref = RKIData_cdr_by_ref_clean

  # Save export RKI dataframe by 'Meldedatum'
  RKIData_cdr_by_melde.to_csv(r'./data/rki/rki-cdr-melde.csv', index = False),
  # Save export RKI dataframe by 'Refdatum'
  RKIData_cdr_by_ref.to_csv(r'./data/rki/rki-cdr-ref.csv', index = False)



if __name__ == "__main__":
  main()