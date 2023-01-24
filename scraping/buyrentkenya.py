from datetime import date
from bs4 import BeautifulSoup
import requests

brk_link = 'https://www.buyrentkenya.com/flats-apartments-for-rent'

# website not working
# brk_page = requests.get(brk_link)

# brk_soup = BeautifulSoup(brk_page.content, 'html.parser')
# div_lists = brk_soup.find_all('div', {'class':"mb-3 w-full"})


# for elephant in div_lists:
#     # date_added = elephant.find('span', {'class':'text-white text-xs'})
#     price = elephant.find('a', class_='no-underline').string
#     description = elephant.find('a', {'class':'no-underline text-black'}).string
#     location = elephant.find('p', {'class':'text-md md:text-sm'}).string
#     bed_rooms = elephant.find('span', {'class':'text-sm mr-5'}).string
#     info = [price, description, location, bed_rooms]
#     print(info)


    




# print(page)