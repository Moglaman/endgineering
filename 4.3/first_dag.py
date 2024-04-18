from airflow import DAG
#from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
from datetime import datetime 

def first_DAG_AirFlow():  
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 
    print("Current Time =", current_time)

default_args = {
    'owner': 'KaygorodcevMYa',
    'start_date': days_ago(1),
}


with DAG(
    dag_id='first_DAG',
    default_args=default_args,
    max_active_runs=1,
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    task = PythonOperator(task_id='first_dag_airFlow', python_callable=first_DAG_AirFlow)

    start >> task >> end