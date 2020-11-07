import urllib.request
import argparse
from bs4 import BeautifulSoup



html = urllib.request.urlopen('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
bsoup = BeautifulSoup(html, "html.parser")

stock_data = bsoup.findAll('tr')

def main():
    
    print("Apple Inc. (AAPL) Daily Closing Prices:")
    for i in stock_data:
        t_data = i.findAll('td', {"class":"yfnc_tabledata1"})
        if len(t_data) is 7:
            date = t_data[0].contents[0]
            close = t_data[6].contents[0]
            print ("Date: {}, Closing Price: {}").format(date, close)

if __name__ == '__main__':
    main()
