import os

import pytest

from prodgpt.data.utils import download_data_to_local


@pytest.mark.skip(reason="Not implemented")
def test_download_data_to_local():
    DATA_URL = ""
    local_filename = download_data_to_local(DATA_URL)
    assert os.path.exists(local_filename)
    assert os.path.isfile(local_filename)
    assert os.path.getsize(local_filename) > 0
