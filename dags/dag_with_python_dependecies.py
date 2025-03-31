from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_numpy():
    import numpy as np
    print(f"numpy version  {np.__version__}")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies',
    start_date=datetime(2025, 3, 31),
    schedule_interval='@daily'
) as dag:
    

    get_numpy_task = PythonOperator(
        task_id='get_numpy',
        python_callable=get_numpy
    )
    

