import requests
import pandas as pd

API_KEY = 'OdgVhj96Fn9XifFAskL2g17l9SXHxBJY9ku8fKDO'  

url = 'https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/'

params = {
    'frequency': 'hourly',
    'data[]': 'value',
    'facets[fueltype][]': 'SUN',
    'facets[respondent][]': 'CAL',  
    'start': '2024-01-01',
    'end': '2024-03-31',
    'api_key': API_KEY
}

response = requests.get(url, params=params)
json_data = response.json()
print(json_data)
if 'response' in json_data and 'data' in json_data['response']:
    df = pd.DataFrame(json_data['response']['data'])
    df.to_csv('data/raw/solar_california_raw.csv', index=False)
    print("✅ Data downloaded and saved.")
else:
    print("❌ Failed to retrieve expected data:")
    print(json_data)