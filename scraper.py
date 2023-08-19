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
link_list = []
#All 15km from uni
kitchener = "https://www.kijiji.ca/b-apartments-condos/kitchener-waterloo/c37l1700212"
london = "https://www.kijiji.ca/b-apartments-condos/london/c37l1700214?sort=dateDesc"
toronto ="https://www.kijiji.ca/b-apartments-condos/city-of-toronto/apartment-rent/k0c37l1700273?sort=dateDesc"
hamilton = "https://www.kijiji.ca/b-apartments-condos/hamilton/apartment-rent/k0c37l80014?sort=dateDesc"
ottawa = 'https://www.kijiji.ca/b-apartments-condos/ottawa/apartment-rent/k0c37l1700185?sort=dateDesc'
guelph = 'https://www.kijiji.ca/b-apartments-condos/guelph/apartment-rent/k0c37l1700242?sort=dateDesc'

#kijiji url
url_to_scrape = guelph
location = "Guelph"

#scrape twice
for i in range(0,13):
    #html request functions & rendering dynamic content
    session = HTMLSession()
    response = session.get(url_to_scrape)
    response.html.render()

    #parsing html data
    soup = BeautifulSoup(response.html.html, 'html.parser')

    #storing repeating info-container content in a list
    listings = soup.find_all('div', class_ ="info-container")

    #open csv file and write header name
    filename = 'guelph.csv'
    f = open(filename, 'a')
    headers = 'Location,Title,Price,Style,Bedrooms,Bathrooms,Size,Air Conditioned  \n'
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
            try:
                style = tag_list[0].text
            except:
                style = "N/A"
            #scrape bedrooms
            try:
                bedrooms = tag_list[1].text
            except:
                bedrooms = "N/A"
            #scrape bathrooms
            try: 
                bathrooms = tag_list[2].text
            except:
                bathrooms = "N/A"
            #clear list
            tag_list.clear()

            #iterate through all items with this tag
            for size in soup.find_all('dd', class_='twoLinesValue-2815147826'):
                size_list.append(size)\
            #ensure size listing is an integer
            try:
                if size_list[3].text == "Yes" or size_list[3].text == "No":
                #scrape size
                    size = size_list[4].text.replace(",","")
                else:
                #scrape size
                    size = size_list[3].text.replace(",","")
            except:
                size = "N/A"
            #scrape air conditioning
            try: 
                air_conditioned = size_list[5].text.replace(",","")
            except:
                air_conditioned = "N/A"
            #clear list
            size_list.clear()

            #write scraped info into csv file
            try:
                f.write(location +', '+ title +', '+price + ', ' + style + ', ' +bedrooms +', ' +bathrooms +', ' +size + ', ' + air_conditioned +'\n')
            except:
                f.write("\n")
        #if not apartment listing, rerun loop
        else: 
            pass

    #next page
    link_list = []
    link = soup.find("div", class_= "pagination")

    newlinks = link.find_all("a", href = True)

    for newlink in newlinks:
        weblink = "https://www.kijiji.ca" + newlink['href']
        link_list.append(weblink)
    url_to_scrape = link_list[i]
    
#close csv file
f.close()


