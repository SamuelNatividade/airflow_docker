from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator



default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def greet(ti):
    first_name = ti.xcom_pull(task_ids = 'get_name', key = 'first_name')
    last_name = ti.xcom_pull(task_ids = 'get_name', key = 'last_name')
    age = ti.xcom_pull(task_ids = 'get_age', key = 'age')
    print(f"Hello World! My name is {first_name} {last_name} and I am {age} years old.")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Samuel')
    ti.xcom_push(key='last_name', value='Ferreira')

def get_age(ti):
    ti.xcom_push(key = 'age', value = 28)


with DAG(
    default_args=default_args,
    dag_id = 'our_first_dag_using_python_operator',
    description='Our first DAG using Python Operator',
    tags=['Example'],
    start_date = datetime(2025, 3, 22, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'first_task', 
        python_callable=greet,
        )
    
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable=get_name
        )
    
    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable=get_age
        )
    
    [task2, task3] >> task1

