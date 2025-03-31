from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_postgres_operator',
    default_args= default_args,
    start_date = datetime(2025, 3, 27),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(task_id = 'create_postgres_table',
                             postgres_conn_id = 'postgres_connection',
                             sql = """"
                                CREATE TABLE IF NOT EXISTS tests.dag_run (
                                dt date,
                                dag_id character varying,
                                primary key (dt, dag_id
                                )
                             """)
    task1                 
            
                             