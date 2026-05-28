from typing import Counter
import requests as re
from bs4 import BeautifulSoup
from lxml import etree

header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

page = re.get(
    "https://www.cbf.com.br/futebol-brasileiro/tabelas/campeonato-brasileiro/serie-a/2026", verify=False,
    headers=header,
)
soup = BeautifulSoup(page.content, "html.parser")
dom = etree.HTML(str(soup))

# print(page.content)

atributos = {'class': 'g'}

time = soup.find_all("strong")
pts = soup.find_all("td",class_="styles_score__xWAJ6")
# jogos = soup.find_all("span", class_="time-sigla")


print('\n')
for indice, times in enumerate(time[2:12:2]):
    print(f'{indice + 1}º {times.text} {pts[indice].text}')
print('\n')