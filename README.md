# COVID-dashboard
An ETL pipeline used to produce a Power BI dashboard based on a dataset continuously checked for updates.

Once the repo is downloaded and requirements installed, run **etl.py** at the desired time interval to extract the [latest COVID dataset from Our World in Data](https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv), perform transformations, and load the processed dataset. This pipeline is is set up to load the processed data into a PostgreSQL table (update the **.env** file in the scripts folder), which is then queried by Power BI. 

**covid dashboard 1_30_26.pdf** is an example export of a dashboard created using the data from this pipeline. 

This repo was made primarily as a personal project; further work is unlikely.
