from typing import Counter
import requests
from bs4 import BeautifulSoup
from lxml import etree
from openpyxl import Workbook

header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

page = requests.get(
    "https://atrativatur.com.br/programacao.php",
    headers=header,
)
soup = BeautifulSoup(page.content, "html.parser")
# soup = BeautifulSoup(html_doc, "html.parser")
dom = etree.HTML(str(soup))

# print(page.content)

# atributos = {'class': 'g'}

# time = soup.find_all("div", class_="table-mes")
tr = soup.find_all("tbody")

# time = soup.find_all("div", class_="table-mes")
# jogos = soup.find_all("span", class_="time-sigla")

for td in tr:
    print(td.find())

# for i, td in enumerate(tr):
#     if i == 6:
#         print(td.get_text())
    

# for td  in tr:
#     print(td.get_text())

    # if mes.text == "Junho":
        # print(mes)
        # print(soup.find_all("tbody"))
        # print(dom.xpath('//*[@id="viagens"]/div[2]/table/tbody/tr[1]/td[2]')[0].text)

        # for td in soup.find_all("tbody"):
        #     print(td.text)




    # for titulo in soup.find_all("th"):        
    #     print(titulo.text)
    

# print('{0:30} ==> {1}'.format('Time', 'Pontos'))
# print('-' * 40)

# for i in range(10):
#     print(f'{time[i].text:30} ==>  {pts[i].text}')
#     print('=' * 40)

# print('\n')
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
#         # print(i + 1, "º ", time_casa[i].text, placar[i].text,
#         #       time_fora[i].text)
#         print(
#             f'{i+1:2}º ==> {time_casa[i].text:4} {placar[i].text} {time_fora[i].text:>4}'
#         )
#         # print(i + 1, "º ", time_casa[i].text, placar[i].text,
#         #       time_fora[i].text)
#     except:
#         print(
#             f'{i + 1:2}º ==> { time_casa[i].text:6} x {time_fora[i].text:>6}')

# print(i + 1, "º", time[i].text, "=>", pts[i + 14].text)
