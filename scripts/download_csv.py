# -*- coding: utf-8 -*-
"""
This is the script for downloading .csv files from the specified URL daily. The downloaded .csv will be given a datestamp.
"""

import requests
from pathlib import Path
from datetime import date
import certifi

#The Website hosting the dataset
URL = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

filename = output_dir / f"data_{date.today()}.csv"

response = requests.get(URL, timeout=30, verify=certifi.where())
response.raise_for_status()

filename.write_bytes(response.content)

print(f"Downloaded {filename}")
