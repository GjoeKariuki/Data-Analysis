# i will use BeautifulSoup to scrape all the 50 pages of a website and create a csv file with 
# the relevant data for analysis

import requests
from bs4 import BeautifulSoup
import pandas as pd

mbooks = []
for i in range(1,51):
    site_url = f'http://books.toscrape.com/catalogue/page-{i}.html'
    site_response = requests.get(site_url)
    site_soup = BeautifulSoup(site_response.content, 'lxml')
    ol_list = site_soup.find('ol')
    ol_articles = ol_list.find_all('article', class_='product_pod')

    
    for art in ol_articles:
        title = (art.find('img')).attrs['alt']
        book_stars = ((art.find('p'))['class'])[1]
        price = float(((art.find('p', class_='price_color')).string).strip('£'))
        mbooks.append([title, book_stars, price])


books_dframe = pd.DataFrame(data = mbooks, columns=['Title','Stars','Price (£)'])
books_dframe.to_csv("bookscrape.csv")

# print(mbooks)