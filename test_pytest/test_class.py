import pytest
import requests


def test_jian():
    a = 3
    b = 2
    assert a - b == 1
    print("a-b" + "1")


class TestMobile:
    def setup_class(self):
        print("start......!!!!")

    def teardown_class(self):
        print("over ------")

    def test_mobilesearch(self):
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

    def test_add(self):
        a = 'nice to meet you!'
        assert 'you' in a
        print("nice to meet you!")


if __name__ == '__main__':
    pytest.main()
