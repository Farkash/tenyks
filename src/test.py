import urllib2
from bs4 import BeautifulSoup
import pandas
import csv

page1 = 'https://www.privateschoolreview.com/alabama'

alabama = urllib2.urlopen(page1)

soup = BeautifulSoup(alabama, "lxml")

target_divs = soup.find_all("div", class_= "school-type-list-text")

for div in target_divs:
    counties = div.find_all("div", class_= "table_cell_county")
    for county in counties:
        print county.text
        print counties.index(county) 

print counties

# print counties[0]