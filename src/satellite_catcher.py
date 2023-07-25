import requests
import os

class SatelliteCatcher:
    def __init__(self, base_url='https://www.space-track.org'):
        self.base_url = base_url
        self.api_username = os.getenv('API_USERNAME')
        self.api_key = os.getenv('API_KEY')

    def catch_sats(self, norad_cat_id):
        tle_endpoint = f'/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/{norad_cat_id}/orderby/EPOCH desc/limit/1/format/tle'
        url = self.base_url + tle_endpoint.replace("{norad_cat_id}", norad_cat_id)
        response = requests.get(url, auth=(self.api_username, self.api_key))
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to get data:', response.status_code)
            return None
