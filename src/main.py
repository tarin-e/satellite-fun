from satellite_catcher import SatelliteCatcher
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

def main():
    satellite_catcher = SatelliteCatcher()
    sat = satellite_catcher.catch_sats("ISS (ZARYA)")
    print(sat)

if __name__ == "__main__":
    main()