from satellite_catcher import SatelliteCatcher
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

def main():
    satellite_catcher = SatelliteCatcher()
    sat = satellite_catcher.catch_sats("25544")
    sat = satellite_catcher.fetch_satcat_data("ISS")
    print(sat)

if __name__ == "__main__":
    main()