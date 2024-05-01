import requests

url = "https://timeapi.io/api/Time/current/zone"
parameters = {"timeZone": "Asia/Seoul"}

response = requests.get(url, params=parameters)

# print(response.text)

import json
import pandas as pd

js = json.loads(response.text)

df = pd.DataFrame(js, index= [0])

print(df)