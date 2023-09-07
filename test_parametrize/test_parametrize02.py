import pytest
import requests
from utils.read_data import get_data


@pytest.mark.parametrize("shouji, appkey", get_data()['mobile'])
def test_mobilesearch(shouji,appkey):
    params = {
        "shouji": shouji,
        "appkey": appkey
    }
    url = 'http://sellshop.5istudy.online/sell/shouji/query'
    r = requests.get(url=url, params=params)
    print(shouji,appkey)
