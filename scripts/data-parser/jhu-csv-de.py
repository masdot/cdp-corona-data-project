import requests
import json
import pandas as pd
from datetime import date


# JHU data via STATWORX covid-19-api
# See more: https://github.com/STATWORX/covid-19-api

# Disable dataframe max for big dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# POST to API for DE-data
payload = {'code': 'DE'}
URL = 'https://api.statworx.com/covid'
response = requests.post(url=URL, data=json.dumps(payload))

# Convert to data frame
jhu_df = pd.DataFrame.from_dict(json.loads(response.text))

today = date.today()

jhu_df.to_csv(f'coviddata_jhu_de_{today}', index=False)

# print(jhu_df.head)

"""
API is outdated --> Last entry 2020-12-14
"""