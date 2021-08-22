from typing import Counter
import requests
from bs4 import BeautifulSoup
from lxml import etree

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

page = requests.get(
    "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021",
    headers=header,
)
soup = BeautifulSoup(page.content, "html.parser")
dom = etree.HTML(str(soup))


# print(page.content)

# soup = BeautifulSoup(page.content, "html.parser")

# atributos = {'class': 'g'}

""" time = soup.find_all("span", class_="hidden-xs")
pts = soup.find_all("th")
jogos = soup.find_all("span", class_="time-sigla") """

# for link in soup.find_all("span"):
# print(link.get("class=time pull-left"))

# print(jogos[38].text)
time_casa = dom.xpath(
    "/html/body/div[1]/main/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/div[1]/span"
)
time_fora = dom.xpath(
    "/html/body/div[1]/main/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/div[2]/span"
)

placar = dom.xpath(
    '//*[@id="menu-panel"]/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/strong/span'
)


for i in range(10):
    # print(time_casa[i].text, placar[i].text, time_fora[i].text)
    try:
        print(
            "Jogo ", i + 1, "º ", time_casa[i].text, placar[i].text, time_fora[i].text
        )
    except:
        print("Jogo ", i + 1, "º ", time_casa[i].text, "  x  ", time_fora[i].text)

# print(i + 1, "º", time[i].text, "=>", pts[i + 14].text)
