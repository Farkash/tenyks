import urllib2
from bs4 import BeautifulSoup
import pandas
import csv

page1 = 'https://www.privateschoolreview.com/alabama'

alabama = urllib2.urlopen(page1)

soup = BeautifulSoup(alabama, "lxml")

target_divs = soup.find_all("div", class_="school-type-list-text")

counties = []
schools = []
students = []
minority = []
for div in target_divs:
    county = div.find_all("div", class_="table_cell_county")
    # print county[0].find(text=True)
    # counties.append(county[0].find(text=True))
    for c in county:
        counties.append(c.text.encode('utf-8'))
    other = div.find_all("div", class_="table_cell_other")
    # schools.append(other[0].find(text=True))
    for s in other:
        schools.append(s[0].text.encode('utf-8'))
    # students.append(other[1].find(text=True))
    # for t in other:
    #     students.append(s.text.encode('utf-8'))
    # minority.append(other[2].find(text=True))
    # for m in other:
    #     minority.append(s.text.encode('utf-8'))

print schools
# df = pandas.DataFrame(counties, columns=['County'])
# df['Schools'] = schools
# df['Students'] = students
# df['Minority'] = minority

# print df

# counties = []
# other_data = []
# for div in target_divs:
#     county = div.find_all("div", class_="table_cell_county")
#     for c in county:
#         counties.append(c.text.encode('utf-8'))
#     other = div.find_all("div", class_="table_cell_other")
#     for i in other:
#         other_data.append(i.text.encode('utf-8'))

# df.to_csv("india-test.csv", encoding = 'utf-8')
