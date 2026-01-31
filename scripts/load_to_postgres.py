# -*- coding: utf-8 -*-
"""
This is the script for loading the processed data into a PostgreSQL server. Configure the .env file with the appropriate credentials.
"""

import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

#Set the values used here in the .env file
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}"
    f"@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
)

df = pd.read_csv("data/processed/clean_data.csv")

df.to_sql(
    "daily_data",
    engine,
    if_exists="append", 
    index=False
)


print("Data loaded into PostgreSQL")
