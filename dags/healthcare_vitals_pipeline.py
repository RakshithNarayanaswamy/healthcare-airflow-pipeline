from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def bronze_done():
    print("Bronze notebook executed in Databricks CE")

def silver_done():
    print("Silver notebook executed in Databricks CE")

def gold_done():
    print("Gold notebook executed in Databricks CE")

def snapshot_done():
    print("Snapshot created in Databricks CE")

def publish_pipeline_event():
    subprocess.run(
        ["python", "/opt/airflow/dags/kafka_event_producer.py"],
        check=True
    )

with DAG(
    dag_id="healthcare_vitals_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    tags=["airflow", "healthcare", "databricks", "kafka"]
) as dag:

    start = EmptyOperator(task_id="start")

    bronze = PythonOperator(
        task_id="vitals_stream_bronze",
        python_callable=bronze_done
    )

    silver = PythonOperator(
        task_id="vitals_stream_silver",
        python_callable=silver_done
    )

    gold = PythonOperator(
        task_id="vitals_stream_gold",
        python_callable=gold_done
    )

    snapshot = PythonOperator(
        task_id="gold_snapshot",
        python_callable=snapshot_done
    )

    publish_event = PythonOperator(
        task_id="publish_pipeline_event",
        python_callable=publish_pipeline_event
    )

    start >> bronze >> silver >> gold >> snapshot >> publish_event