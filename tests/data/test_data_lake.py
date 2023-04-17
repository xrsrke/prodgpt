from prodgpt.data.data_lake import DataLake


def test_upload_to_data_lake(config):
    bucket_name = config["gcloud_storage"]["bucket_name"]
    data_lake = DataLake(bucket_name=bucket_name)

    data_lake.upload()


def test_read_from_data_lake():
    pass
