import requests

class SatelliteCatcher:
    def __init__(self, base_url='https://www.space-track.org'):
        self.base_url = base_url

    def catch_sats(self, norad_cat_id):
        tle_endpoint = '/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/{norad_cat_id}/orderby/EPOCH desc/limit/1/format/tle'
        response = requests.get(f'{self.base_url}/tle_endpoint')
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to get data:', response.status_code)
            return None
        
