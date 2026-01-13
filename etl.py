#ChatGPT's master file for running the ETL pipeline.

import subprocess

subprocess.run(["python", "scripts/download_csv.py"], check=True)
subprocess.run(["python", "scripts/transform.py"], check=True)
subprocess.run(["python", "scripts/load_to_postgres.py"], check=True)
