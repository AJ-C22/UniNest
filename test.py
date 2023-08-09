

url_to_scrape = "https://www.kijiji.ca/b-apartments-condos/kitchener-waterloo/apartment-rent-in-kitchener/k0c37l1700212?sort=dateDesc&radius=15.0&address=University+of+Waterloo%2C+University+Avenue+West%2C+Waterloo%2C+ON&ll=43.472285%2C-80.544858"
hash = url_to_scrape
hash = hash[:88] + '/page-2' + hash[88:]
url_to_scrape = hash 
print(url_to_scrape)

for i in range(1,3):
    print('hi')