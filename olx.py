import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from lxml import etree

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-pe/regiao-de-petrolina-e-garanhuns/petrolina?pe=50000&q=celta'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

try:
        req = Request(url, headers= headers)
        response = urlopen(req)
        html = response.read()

except HTTPError as e:
        print(e.status, e.reason)

# except URLerror as e:
#         print(e.reason)

soup = BeautifulSoup(html, 'lxml')

# soup = BeautifulSoup(page.content, 'html.parser')
# dom = etree.HTML(str(soup))

# Criando uma planilha Excel
wb = Workbook()
ws = wb.active
ws.append(['Anúncio'])

ad_details = soup.find_all('section')
title = soup.find_all('a',class_='olx-ad-card__title-link')
preco  = soup.find_all('h3',class_='olx-text olx-text--body-large olx-text--block olx-text--semibold olx-ad-card__price')
km = soup.find_all('div',class_='olx-ad-card__details-ads olx-ad-card__details-ads--vertical')

total = len(title)
y=0
for i in range(total):
        y += 1
        # print(title[i].text, preco[i].text)
        # print(km[i].text)
        print(y, km[i].text, preco[i].text )

# for i in ad_details:
        
# Extraindo e categorizando os dados
# for ad in ad_details:
#   print(ad.text)
#   title = ad.find('a',class_='olx-ad-card__title-link')
#   print(title.text)
#   price = ad.find('span', class_='sc-7l84qu-2 bLOqvD').text.strip()
#   price = ad.find('span', class_='olx-ad-card__old-price--fixed').text.strip()
#   ws.append([title])


#   if 'celular' in title.lower():
#       category = 'Eletrônicos'
#   elif 'carro' in title.lower() or 'moto' in title.lower():
#       category = 'Veículos'
#   elif 'sofá' in title.lower() or 'mesa' in title.lower():
#       category = 'Móveis'
#   else:
#       category = 'Outros'

# Salvando a planilha
# wb.save('dados_olx.xlsx')