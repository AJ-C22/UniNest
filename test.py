import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import csv



link_list = ['https://www.kijiji.ca/b-apartments-condos/london/page-2/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-3/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-4/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-5/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-6/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-7/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-8/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-9/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-10/c37l1700214', 'https://www.kijiji.ca/b-apartments-condos/london/page-2/c37l1700214', 'https://www.kijiji.ca/rss-srp-apartments-condos/london/c37l1700214']
link_list1 = []
kitchener = "https://www.kijiji.ca/b-apartments-condos/london/c37l1700214?sort=dateDesc"
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


