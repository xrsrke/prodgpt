from google.cloud import storage


class DataLake:
    def __init__(
        self,
        bucket_name: str
    ):
        storage_client = storage.Client()

        self.bucket_name = bucket_name
        self.bucket = storage_client.bucket(bucket_name)

    def is_file_exists(self, file_name: str):
        blob = self.bucket.blob(file_name)
        return blob.exists()

    def upload_single_file(
        self,
        source_file_name: str,
        destination_blob_name: str
    ):
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        return blob

    def retrieve_single_file(self, file_name: str):
        blob = self.bucket.blob(file_name)
        return blob.download_as_string()

    def delete_single_file(self, file_name: str):
        blob = self.bucket.blob(file_name)
        return blob.delete()

    def download(self, file_name: str, destination_file_name: str):
        blob = self.bucket.blob(file_name)
        return blob.download_to_filename(destination_file_name)
