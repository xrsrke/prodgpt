def download_data_to_local(url: str) -> str:
    import os
    import tempfile

    import requests

    local_filename = os.path.join(tempfile.gettempdir(), "input.txt")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return local_filename


def read_data_from_local(local_filename: str) -> str:
    with open(local_filename, "r") as f:
        return f.read()
