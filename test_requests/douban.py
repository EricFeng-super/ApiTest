import requests

url = 'https://www.douban.com/search'
params = {
    "q": "教父"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
r = requests.get(url=url, params=params, headers=headers)
print(r.status_code)
print(r.text)
