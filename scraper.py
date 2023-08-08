import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import csv

#tag lists
tag_list=[]
size_list =[]

#kitchener = "https://www.kijiji.ca/b-kitchener-waterloo/apartment-rent-in-kitchener/k0l1700212"
#london = "https://www.kijiji.ca/b-apartments-condos/ontario/london/k0c37l9004"

#All 15km from uni
kitchener = "https://www.kijiji.ca/b-apartments-condos/kitchener-waterloo/apartment-rent-in-kitchener/k0c37l1700212?sort=dateDesc&radius=15.0&address=University+of+Waterloo%2C+University+Avenue+West%2C+Waterloo%2C+ON&ll=43.472285%2C-80.544858"
london = "https://www.kijiji.ca/b-apartments-condos/london/london/k0c37l1700214?sort=dateDesc&radius=15.0&address=Western+University%2C+Richmond+St%2C+London%2C+ON&ll=43.00959710000001%2C-81.2737336"
toronto ="https://www.kijiji.ca/b-apartments-condos/city-of-toronto/apartment-for-rent/k0c37l1700273?sort=dateDesc&radius=15.0&address=University+of+Toronto%2C+King%27s+College+Circle%2C+Toronto%2C+ON&ll=43.6633848%2C-79.3960062"
hamilton = "https://www.kijiji.ca/b-apartments-condos/hamilton/apartment-for-rent/k0c37l80014?address=McMaster%20University%2C%20Main%20Street%20West%2C%20Hamilton%2C%20ON&ll=43.260879%2C-79.9192254&radius=15.0&sort=dateDesc"
ottawa = 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-for-rent/k0c37l1700185?sort=dateDesc&radius=15.0&address=University+of+Ottawa%2C+Laurier+Ave+E%2C+Ottawa%2C+ON&ll=45.4231064%2C-75.68313289999999'
guelph = 'https://www.kijiji.ca/b-apartments-condos/guelph/apartment-for-rent/k0c37l1700242?sort=dateDesc&radius=15.0&address=University+of+Guelph%2C+Stone+Road+East%2C+Guelph%2C+ON&ll=43.5327217%2C-80.22618039999999'

#kijiji url
url_to_scrape = kitchener

#html request functions & rendering dynamic content
session = HTMLSession()
response = session.get(url_to_scrape)
response.html.render()

#parsing html data
soup = BeautifulSoup(response.html.html, 'html.parser')

#storing repeating info-container content in a list
listings = soup.find_all('div', class_ ="info-container")

#open csv file and write header name
filename = 'kitchener.csv'
f = open(filename, 'w')
headers = 'Title,Price,Style,Bedrooms,Bathrooms,Size,Air Conditioned  \n'
f.write(headers)

print("check 1")

#loop through every listing on the page to scrape info
for listing in listings:

    print("check 2")
    #scrape title 
    title = listing.find('div', class_="title").text
    title =title.strip()
    title = title.replace(",","")

    print("check 3")
    #scrape price
    price = listing.find('div', class_="price").text
    price = price.strip()
    price = price.replace(",", "")

    #scrape nested link
    link = listing.find("a", href = True)
    weblink = "https://www.kijiji.ca" + link['href']
    print(weblink)

    #ensure nested link is for apartment listings
    if weblink.find("v-apartments-condos") > 0:
        
        #set nested link as new weblink
        response = session.get(weblink)
        response.html.render()
        soup = BeautifulSoup(response.html.html, 'html.parser')
        
        #iterate through all items with this tag
        for tag in soup.find_all('li', class_='noLabelAttribute-2328647506'):
            tag_list.append(tag)
        #scrape style
        style = tag_list[0].text
        #scrape bedrooms
        bedrooms = tag_list[1].text
        #scrape bathrooms
        bathrooms = tag_list[2].text
        #clear list
        tag_list.clear()

        #iterate through all items with this tag
        for size in soup.find_all('dd', class_='twoLinesValue-2815147826'):
            size_list.append(size)\
        #ensure size listing is an integer
        if size_list[3].text == "Yes" or size_list[3].text == "No":
            #scrape size
            size = size_list[4].text.replace(",","")
        else:
            #scrape size
            size = size_list[3].text.replace(",","")
        #scrape air conditioning
        air_conditioned = size_list[5].text.replace(",","")
        #clear list
        size_list.clear()

        #write scraped info into csv file
        f.write(title +', '+price + ', ' + style + ', ' +bedrooms +', ' +bathrooms +', ' +size + ', ' + air_conditioned +'\n')

    #if not apartment listing, rerun loop
    else: 
        pass
    
#closse csv file
f.close()


