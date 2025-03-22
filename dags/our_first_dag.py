from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
     'retries': 5,
      'retry_delay': timedelta(minutes=2)
      }


with DAG(
    dag_id="our_first_dag",
    description="Our first DAG",
    default_args=default_args,
    tags=["Example"],
    start_date=datetime(2025, 3, 22, 2),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(task_id = "first_task", 
                         bash_command = "echo Hello World!")
    

    task2 = BashOperator(task_id = "second_task",
                            bash_command = "echo Hello World 2!")
    
                        
    task3 = BashOperator(task_id = "third_task",
                         bash_command = "echo Hello World 3!")
    


    # Task Dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task Dependency method 2
    # task1 >> task2 
    # task1 >> task3

    # Task Dependency method 3
    task1 >> [task2, task3]
    

