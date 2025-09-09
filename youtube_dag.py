from __future__ import annotations
from datetime import timedelta, datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from youtube_etl import run_etl_workflow

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="youtube_dag",
    default_args=default_args,
    description="A DAG to run the YouTube ETL process.",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="0 12 * * *",  # Run once a day at noon UTC
    catchup=False,
    tags=["youtube", "etl"],
) as dag:
    
    run_etl = PythonOperator(
        task_id="complete_youtube_etl",
        python_callable=run_etl_workflow,
    )
