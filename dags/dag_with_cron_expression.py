from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}



with DAG(
    default_args = default_args,
    dag_id = 'dag_with_cron_expression',
    start_date = datetime(2025, 3, 15),
    schedule_interval = '0 3 * * Tue'
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'echo Simple bash command with cron expression'
    )
