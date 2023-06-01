from airflow.decorators import dag
from airflow.providers.airbyte.operators.airbyte import \
    AirbyteTriggerSyncOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "catch_up": False,
}


@dag(
    dag_id="dataops",
    default_args=default_args,
    start_date=days_ago(1)
)
def dataops():
    extract_and_load_projects = AirbyteTriggerSyncOperator(
        task_id="extract_and_load_projects",
        airbyte_conn_id="airbyte",
        connection_id="53780561-ce8f-4079-82df-465943ce5a71",  # REPLACE
        asynchronous=False,
        timeout=3600,
        wait_seconds=3,
    )

    extract_and_load_projects


do = dataops()
