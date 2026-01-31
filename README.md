# COVID-dashboard
An ETL used to produce a PowerBI dashboard based on a dataset checked daily.

Once the repo is downloaded, run **etl.py** at the desired time interval to extract the [latest COVID dataset from Our World in Data](https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv), perform transformations, and load the processed dataset. This pipeline is is set up to load the processed data into a PostgreSQL table, which is then queried by Power BI. **
