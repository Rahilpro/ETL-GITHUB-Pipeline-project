from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, "/Users/rahil/Desktop/etl")
os.chdir("/Users/rahil/Desktop/etl")

default_args = {
    "owner":       "rahil",
    "retries":     2,
    "retry_delay": timedelta(minutes=5),
}

def run_etl():
    from dotenv import load_dotenv
    load_dotenv("/Users/rahil/Desktop/etl/.env")
    from connector import run_pipeline
    run_pipeline()

with DAG(
    dag_id="github_etl",
    default_args=default_args,
    description="Nightly GitHub repo ETL with quality checks",
    schedule="0 2 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["etl", "github"],
) as dag:

    etl_task = PythonOperator(
        task_id="extract_load_validate",
        python_callable=run_etl,
    )
