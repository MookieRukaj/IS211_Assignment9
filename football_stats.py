import urllib.request
import argparse
from bs4 import BeautifulSoup


def football_stats():
    
    html = urllib.request.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2020-season-regular-category-touchdowns")
    response = html.read()
    soup = BeautifulSoup(response, 'html.parser')
    data = soup.find_all(class_={'row1', 'row2'})[:20]
    stats = 'Player: {} -> Position: {} -> Team: {} -> Touchdowns: {}'
    for row in data:
        print(stats.format(row.contents[0].text, row.contents[1].text,
                           row.contents[2].text, row.contents[6].text))


