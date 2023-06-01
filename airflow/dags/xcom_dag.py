from datetime import datetime

from airflow.operators.python import PythonOperator

from airflow import DAG


def task_1(ti):
    x = 2
    ti.xcom_push(key="x", value=x)


def task_2(ti):
    x = ti.xcom_pull(key="x", task_ids=["task_1"])[0]
    y = x + 3
    ti.xcom_push(key="y", value=y)


with DAG(
    dag_id="xcom_dag",
    start_date=datetime.today(),
) as dag:
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=task_1,
    )

    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=task_2,
    )

    task_1 >> task_2
