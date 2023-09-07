import requests

params = {
    "shouji": '18918919441',
    "appkey": '0c818521d38759e1'
}
r = requests.get(url='http://sellshop.5istudy.online/sell/shouji/query', params=params)
print(r.status_code)

data = {
    "text": "jackson"
}
r = requests.post(url='https://dict.youdao.com/keyword/key', data=data)
print(r.text)

json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
r = requests.post(url='https://jsonplaceholder.typicode.com/posts', json=json_data)
print(r.status_code)
print(r.json())
