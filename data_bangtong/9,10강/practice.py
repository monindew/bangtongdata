import requests

response = requests.get("https://www.imdb.com/chart/top/", headers={"User-Agent": "Chrome"})

print(response.status_code)
print(response.text)