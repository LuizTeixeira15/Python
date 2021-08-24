from typing import Counter
import requests
from bs4 import BeautifulSoup
from lxml import etree

header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

page = requests.get(
    "https://ge.globo.com/futebol/brasileirao-serie-a/",
    headers=header,
)

soup = BeautifulSoup(page.content, "html.parser")
dom = etree.HTML(str(soup))

# print('{0:30} ==> {1}'.format('Time', 'Pontos'))
# print('-' * 40)

# for i in range(5):
#     print(f'{time[i].text:30} ==>  {pts[i + 14].text}')
#     print('=' * 40)

print(
    dom.xpath(
        '#classificacao__wrapper > article > section.tabela.tabela__pontos-corridos > div > table.tabela__equipes.tabela__equipes--com-borda > tbody > tr:nth-child(1) > td.classificacao__equipes.classificacao__equipes--time > strong'
    ))

# time_casa = dom.xpath(
#     "/html/body/div[1]/main/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/div[1]/span"
# )
# time_fora = dom.xpath(
#     "/html/body/div[1]/main/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/div[2]/span"
# )

# placar = dom.xpath(
#     '//*[@id="menu-panel"]/article/div[1]/div/div/section[1]/div[2]/aside/div/div[17]/div/ul/li/div/div/a/strong/span'
# )

# for i in range(10):
#     # print(time_casa[i].text, placar[i].text, time_fora[i].text)
#     try:
#         print(i + 1, "º ", time_casa[i].text, placar[i].text,
#               time_fora[i].text)
#     except:
#         print(i + 1, "º ", time_casa[i].text, "  x  ", time_fora[i].text)

# print(i + 1, "º", time[i].text, "=>", pts[i + 14].text)
