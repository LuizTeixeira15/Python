from selenium import webdriver

import request

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

page = request.get("https://ge.globo.com/futebol/brasileirao-serie-a", headers=headers)

 print(page.content)
  
 soup = BeautifulSoup(page.content, 'html.parser')

  atributos = {'class': 'g'}

 respostas = soup.find_all("tdoby", class_="classificacao__tabela--linha")

 print(respostas)
