import pandas as pd
from datetime import date

# RKI data via CSV (daily updated)
# See more: https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv

# Disable dataframe max for big dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Set status for 0p-to-dateness
"""
status:
0: not up to date
1: up to date and checked (todays date == date[Datenstand])
"""
status = 0

#* Convert csv to dataframe
rki_df = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv');

#* Check for plausibility

# Check last row
last_row = rki_df.iloc[-1]
last_datenstand = last_row['Datenstand']
#? (Example date:  04.04.2021, 00:00 Uhr)
last_meldedatum = last_row['Meldedatum']

# Get todays date
date_today = date.today()
# Formatting todays date
check_datenstand = (date_today.strftime("%d.%m.%Y") + ', 00:00 Uhr')

print(last_datenstand)
print(check_datenstand)

if last_datenstand == check_datenstand:
    status = 1
    #* Save dataframe as csv named with date
    today = date.today()
    rki_df.to_csv(f'coviddata_rki_de_{today}', index=False)
    # print('up to date!')

else:
    status = 0
    print('not up to date!')

## Plotting

