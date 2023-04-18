from typing import Union

from prodgpt.data.data_lake import DataLake

GCLOUD_DEFAULT_PATH = "testing/"
TESTING_FILE_PATH = "not_delete/persistence.txt"


def create_a_random_local_txt_file(content: str) -> Union[str, str]:
    import os
    import random
    import string

    file_name = "".join(random.choices(string.ascii_lowercase, k=10)) + ".txt"
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, "w") as f:
        f.write(content)

    return file_path, file_name


def delete_a_local_file_from_file_path(file_path):
    import os

    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f'Error: file "{file_path}" not found.')
    except Exception as e:
        print(f'Error deleting file "{file_path}": {str(e)}')


def is_local_file_exist(file_path):
    import os

    return os.path.exists(file_path)


def test_create_delete_a_random_local_txt_file_then_delete_it():
    FILE_CONTENT = "Persistence is all you need"
    file_path, file_name = create_a_random_local_txt_file(FILE_CONTENT)

    assert file_path is not None
    assert file_name is not None
    assert is_local_file_exist(file_path) is True

    delete_a_local_file_from_file_path(file_path)

    assert is_local_file_exist(file_path) is False


def test_is_file_exists(config):
    BUCKET_NAME = config["gcloud_storage"]["bucket_name"]
    FILE_PATH = "not_delete/avatar.png"

    data_lake = DataLake(bucket_name=BUCKET_NAME)

    assert data_lake.is_file_exists(FILE_PATH) is True


def test_upload_retrieve_delete_a_single_file_to_data_lake(config):
    BUCKET_NAME = config["gcloud_storage"]["bucket_name"]
    FILE_CONTENT = "Persistence is all you need"

    data_lake = DataLake(bucket_name=BUCKET_NAME)
    src_path, file_name = create_a_random_local_txt_file(FILE_CONTENT)
    dest_path = GCLOUD_DEFAULT_PATH + file_name

    data_lake.upload_single_file(src_path, dest_path)

    assert data_lake.is_file_exists(dest_path) is True
    assert data_lake.retrieve_single_file(dest_path) == FILE_CONTENT.encode()
    assert data_lake.delete_single_file(dest_path) is None
    assert data_lake.is_file_exists(dest_path) is False

    delete_a_local_file_from_file_path(src_path)
