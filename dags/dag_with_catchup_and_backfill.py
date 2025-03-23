from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = 'dag_with_catchup_and_backfill',
    default_args = default_args,
    schedule_interval = '@daily',
    start_date = datetime(2025, 3, 23),
    catchup = False
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'echo Simple bash command'
    )

