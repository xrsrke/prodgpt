from datetime import datetime

from airflow.decorators import dag, task


@dag(dag_id="new_example", start_date=datetime.today())
def new_example():
    @task
    def get_name():
        pass

    @task
    def get_age():
        pass

    @task
    def greet(name, age):
        print("hello")

    name = get_name()
    age = get_age()
    greet(name=name, age=age)


instance = new_example()
