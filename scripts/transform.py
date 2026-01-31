# -*- coding: utf-8 -*-
"""
This is the script for processing/data cleaning of the raw data files. The most recent raw dataset will be processed and saved in a new file.
"""

import pandas as pd
from pathlib import Path

#Select the newest dataset for processing.
raw_file = max(Path("data/raw").glob("data_*.csv"))
df = pd.read_csv(raw_file)

#Cleaning (possibly expand later if other issues identified)

#Fill missing values with -99 (actually save this change with inplace True)
df.fillna(value=-99,inplace=True)

output_path = Path("data/processed/clean_data.csv")
output_path.parent.mkdir(exist_ok=True)

df.to_csv(output_path, index=False)

print("Data cleaned and saved")
