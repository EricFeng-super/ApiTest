import pytest
import requests


@pytest.fixture(autouse=True)  # 默认scope就是function
def func():
    print("我是前置步骤")


def test_mobilesearch():
    params = {
        "shouji": '18918919441',
        "appkey": '0c818521d38759e1'
    }
    url = 'http://sellshop.5istudy.online/sell/shouji/query'
    r = requests.get(url=url, params=params)
    assert r.status_code == 200
    assert r.json()["status"] == 0
    assert r.json()["msg"] == 'ok'
    print("test mobile")


def test_add():
    a = 'nice to meet you!'
    assert 'you' in a
    print('nice to meet you!')


if __name__ == '__main__':
    pytest.main()
