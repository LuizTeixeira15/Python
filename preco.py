import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
# import re


url =f'https://pt.aliexpress.com/w/wholesale-Placas-gr%C3%A1ficas.html?spm=a2g0o.productlist.allcategoriespc.80.6d10sdqTsdqTNe&categoryUrlParams=%7B%22q%22%3A%22Placas%20gr%C3%A1ficas%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22categoryNagivateOld%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22c8792a24-7ae0-4d2f-b9a8-b4d1b6d7e7ba%22%2C%22scene_id%22%3A%2230630%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22pt%22%2C%22bizScene%22%3A%22categoryNagivateOld%22%2C%22guideModule%22%3A%22unknown%22%2C%22postCatIds%22%3A%227%2C21%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y'

headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
list = soup.find(id = "card-list")

print(list.prettify())
