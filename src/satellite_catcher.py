import requests
import os

class SatelliteCatcher:
    def __init__(self, base_url='https://www.space-track.org'):
        self.base_url = base_url
        self.api_username = os.getenv('API_USERNAME')
        self.api_key = os.getenv('API_KEY')

    def catch_sats(self, norad_cat_id):
        # Construct the API request URL
        tle_endpoint = "/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/{norad_cat_id}/orderby/EPOCH desc/limit/1/format/tle"
        url = self.base_url + tle_endpoint.replace("{norad_cat_id}", norad_cat_id)

        # Send GET request with authentication
        response = requests.get(url, auth=(self.api_username, self.api_key))

        # Check if the request was successful
        if response.status_code == 200:
            data = response.text
            # Process the data as needed
            return data
        else:
            print("Failed to fetch TLE data. Status code:", response.status_code)
            return None
        
    # Function to fetch SATCAT data
    def fetch_satcat_data(self, satellite_intdes):
        # Construct the API request URL
        satcat_endpoint = "/basicspacedata/query/class/satcat/INTDES/{satellite_intdes}/orderby/SATNAME/format/json"
        url = self.base_url + satcat_endpoint.replace("{satellite_intdes}", satellite_intdes)

        # Send GET request with authentication
        response = requests.get(url, auth=(self.api_username, self.api_key))

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Process the data as needed
            return data
        else:
            print("Failed to fetch SATCAT data. Status code:", response.status_code)
            return None
