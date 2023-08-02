from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.kijiji.ca/b-kitchener-waterloo/apartment-rent-in-kitchener/k0l1700212"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

house_title = html_soup.find_all('div', class_ = "realEstateTitle-1440881021" )

for title in house_title:
    title = title.find('div', class_ ="titleRow-4059548442").text
    price = title.find('div', class_ = "priceWrapper-1165431705").text

house_unit = html_soup.find_all('div', class_ = "unitRow-1281171205")

for unit in house_unit:
    style = unit.find('li', class_ = "noLabelAttribute-2328647506").text
    bedrooms = unit.find('span', class_ = "noLabelValue-3861810455").text
    bathrooms = unit.find('span', class_ = "noLabelValue-3861810455").text

