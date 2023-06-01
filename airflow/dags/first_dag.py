from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from airflow import DAG

with DAG(dag_id="hello_3", start_date=days_ago(2)) as dag:
    task1 = BashOperator(
        task_id="hello_world_1",
        bash_command="echo hello world"
    )

    task2 = BashOperator(
        task_id="hello_world_2",
        bash_command="echo hello world"
    )

    task3 = BashOperator(
        task_id="hello_world_3",
        bash_command="echo hello world"
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)
