#Figure out how to scrape into other pages 
#Dyanmic scraping w selenium
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.kijiji.ca/b-apartments-condos/kitchener-waterloo/c37l1700212"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

house_title = html_soup.find_all('div', class_ ="sc-df900376.gsWCmx")
print(house_title)
filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for main in house_title:
    print("hello")
    title = main.find('div', class_="sc-dab8bd1-0 bThYNJ").text
    #price = main.find('h3', attrs={'data-testid': 'listing-title'}).text

    f.write(title)

f.close()
print(page_html)

'''
house_unit = html_soup.find_all('div', class_ = "unitRow-1281171205")


for unit in house_unit:
    style = unit.find('li', class_ = "noLabelAttribute-2328647506").text
    bedrooms = unit.find('span', class_ = "noLabelValue-3861810455").text
    bathrooms = unit.find('span', class_ = "noLabelValue-3861810455").text
'''
