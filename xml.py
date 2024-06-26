import requests
import json

# print(os.path.realpath(__file__))

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

url = "https://script.google.com/macros/s/AKfycbySC5SkEYzn36O5CWNLMOiPTJZSN33dwDGhwYcJN_MYhSsq2ROK2JVqUq67ZLv4TRiX/exec"
headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

def buscar():
    req = requests.get(url)
    todos  = json.loads(req.content)
    # print(todos)
    for i, c in enumerate(req):
        # print(i)
        print(f"{i} - {todos['out'][i]['cte']}")


buscar()