import requests
from bs4 import BeautifulSoup


url = ('https://finance.yahoo.com/quote/0001.HK?p=0001.hk&.tsrc=fin-srch')

res_output = requests.get(url)
web_conts = BeautifulSoup(res_output.text, 'lxml')
web_outta = web_conts.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px) W(100%)')


print(web_outta)
# print(res_output.text)