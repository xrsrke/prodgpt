from datetime import datetime

from airflow.operators.bash import BashOperator

from airflow import DAG

LOCAL_DATA = "/app/prodgpt/data"
DATALAKE_REPO = "/app/prodgpt/prodgpt-data"


with DAG(
    dag_id="local_data_to_data_lake",
    start_date=datetime(2023, 6, 1)
):

    # create a new folder name
    # current_time = datetime.now()
    # FOLDER_NAME = current_time.strftime("%Y_%m_%d_%H%M%S%f")
    FOLDER_NAME = "new_folder"

    create_new_folder_for_new_data = BashOperator(
        task_id="create_new_folder_for_new_data",
        bash_command=f"cd {DATALAKE_REPO} && mkdir {FOLDER_NAME}",
    )

    move_data_to_repo = BashOperator(
        task_id="move_data_to_repo",
        bash_command=f"mv {LOCAL_DATA}/* {DATALAKE_REPO}/{FOLDER_NAME}",
    )

    install_dvc = BashOperator(
        task_id="install_dvc",
        bash_command="pip install dvc",
    )

    add_to_dvc = BashOperator(
        task_id="add_to_dvc",
        bash_command=f"cd {DATALAKE_REPO} && dvc add {FOLDER_NAME} && \
            dvc config core.autostage true",
    )

    push_to_dvc = BashOperator(
        task_id="push_to_dvc",
        bash_command=f"cd {DATALAKE_REPO} && dvc push",
    )

    add_and_push_to_git = BashOperator(
        task_id="add_to_git",
        bash_command=f"cd {DATALAKE_REPO} && git add . && \
            git commit -m 'Add data' && git push",
    )

    create_new_folder_for_new_data >> move_data_to_repo >> install_dvc
    install_dvc >> add_to_dvc
    add_to_dvc >> push_to_dvc >> add_and_push_to_git
