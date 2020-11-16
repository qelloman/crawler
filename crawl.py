from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("all_list.html"), "html.parser")
entries = soup.find_all('div', {"class":"lot-container"})
f = open("artworks.csv", "w")

for entry in entries:
    lot_num_raw = entry.find('p', {"class":"hidden-xs"}).text
    lot_num_search = re.search('(\d+)', lot_num_raw, re.IGNORECASE)
    if lot_num_search:
        lot_num = lot_num_search.group(1)
        #print (lot_num)

    title = entry.find('a', {"class":"sln_lot_show"})['title'].strip()
    #print(title)
 
    price = entry.find_all('span', {"ng-show":"currency == 'USD'"})
    if len(price) > 1:
        hammer_price_raw = price[1].text.strip()
    else:
        hammer_price_raw = price[0].text.strip()
    hammer_price_search = re.search('\$ (.*)', hammer_price_raw, re.IGNORECASE)
    if hammer_price_search:
        hammer_price = hammer_price_search.group(1).replace(',', '')
        #print (hammer_price)
    else:
        hammer_price = "Not_Listed"
    text = entry.find_all('p', {"class":"visible-xs"})
    auction_raw = text[0].text.strip()
    auction_search = re.search('(.*)\n\s+,\s+(.*)', auction_raw, re.IGNORECASE)
    if auction_search:
        auction_house = auction_search.group(1)
        auction_date = auction_search.group(2)
        #print (auction_house)
        #print (auction_date)
        
    country = text[1].text.strip()
    #print(country)
    f.write('|'.join([lot_num,title,hammer_price,auction_house,auction_date,country]))
    f.write("\n")
