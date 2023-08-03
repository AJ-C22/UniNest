from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.kijiji.ca/v-apartments-condos/kitchener-waterloo/luxury-1-bedroom-apartment-for-rent/1658473493"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

house_title = html_soup.find_all('div', class_="realEstateTitle-1440881021" )

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for main in house_title:
    title = main.find('h1', class_="title-2323565163").text
    price = main.find('div', class_= "priceWrapper-1165431705").text

    f.write(title + ', ' + price)

f.close()

'''
house_unit = html_soup.find_all('div', class_ = "unitRow-1281171205")


for unit in house_unit:
    style = unit.find('li', class_ = "noLabelAttribute-2328647506").text
    bedrooms = unit.find('span', class_ = "noLabelValue-3861810455").text
    bathrooms = unit.find('span', class_ = "noLabelValue-3861810455").text
'''
