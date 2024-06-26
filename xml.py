import os
import responses
import json
import requests

# print(os.path.realpath(__file__))

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

url = "https://script.google.com/macros/s/AKfycbySC5SkEYzn36O5CWNLMOiPTJZSN33dwDGhwYcJN_MYhSsq2ROK2JVqUq67ZLv4TRiX/exec"
headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

response = requests.request("GET",url,headers=headers)
t = response.json()
# t = json.dumps(t)
# res = json.loads(t)
print(t['out'][1])
# for i, r in enumerate(res):
#     print(res[i])