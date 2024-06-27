import requests
import json

# print(os.path.realpath(__file__))

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

url = "https://script.google.com/macros/s/AKfycbz815KyVklSpA229FtAUWFvLD8wj6CMwslMUlqz1SPMjNiXgZZ9gx0sbMvXKMWgHBBpdQ/exec?dest=maria"
headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

# def buscar():
req = requests.get(url)
todos  = json.loads(req.content)

print(todos)
# for i, c in enumerate(todos['out']):
#     if todos['out'][i]['cte'] == 22084:
#       print(f"{i} - {todos['out'][i]['cte']}")


# buscar()