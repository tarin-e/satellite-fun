import requests

class SatelliteCatcher:
    def __init__(self, base_url='https://jsonplaceholder.typicode.com'):
        self.base_url = base_url

    def get_posts(self):
        response = requests.get(f'{self.base_url}/posts')
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to get data:', response.status_code)
            return None

if __name__ == "__main__":
    catcher = SatelliteCatcher()
    posts = catcher.get_posts()
    print(posts)