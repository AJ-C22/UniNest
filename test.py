import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import csv



link_list = ['https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-2/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-3/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-4/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-5/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-6/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-7/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-8/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-9/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-10/k0c37l1700185', 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/page-2/k0c37l1700185', 'https://www.kijiji.ca/rss-srp-apartments-condos/ottawa/apartment-rent/k0c37l1700185']
link_list1 = []
kitchener = "https://www.kijiji.ca/b-apartments-condos/guelph/apartment-rent/k0c37l1700242?sort=dateDesc"
url_to_scrape = kitchener
session = HTMLSession()
response = session.get(url_to_scrape)
response.html.render()

soup = BeautifulSoup(response.html.html, 'html.parser')

link = soup.find("div", class_= "pagination")

newlinks = link.find_all("a", href = True)

for newlink in newlinks:
    weblink = "https://www.kijiji.ca" + newlink['href']
    link_list1.append(weblink)

print(link_list1)


