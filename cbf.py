import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

page = requests.get(
    "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021", headers=header)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# # atributos = {'class': 'g'}

respostas = soup.find_all("span", class_="hidden-xs")

print(respostas[4].text)
