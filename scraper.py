from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.kijiji.ca/b-kitchener-waterloo/apartment-rent-in-kitchener/k0l1700212"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

house_price = html_soup.find_all('div', class_ = "priceWrapper-1165431705" )
