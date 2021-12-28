import pytest
import requests as requests

from src import config


@pytest.mark.usefixtures("restart_api")
def test_api_index():
    url = config.get_api_url()
    r = requests.get(f"{url}")
    assert r.status_code == 200
    assert r.text == "i"
