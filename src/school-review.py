import urllib2
from bs4 import BeautifulSoup
import pandas
import csv

page1 = 'https://www.privateschoolreview.com/alabama'

alabama = urllib2.urlopen(page1)

soup = BeautifulSoup(alabama, "lxml")

# soup is one object here, not a list of objects, so we 
# can apply the find_all function to it once. Don't need to loop at all
target_divs = soup.find_all("div", class_="school-type-list-text")

# declare lists
county = []
schools = []
students = []
minority = []


# since target_divs is a list of divs, we need to loop over each item to 
# perform any functions on the entire list
for div in target_divs:
    # counties = div.find("div", class_="table_cell_county")
    # county.append(counties)
    county.append(div.find("div", class_="table_cell_county"))

county = filter(None, county)
for i in range(0, len(county)):
    county[i] = county[i].text

    # print county[0].find(text=True)
    # counties.append(county[0].find(text=True))
    # for c in counties:
        # county.append(c.text.encode('utf-8'))
    # other = div.find_all("div", class_="table_cell_other")
    # schools.append(other[0].find(text=True))
    # for s in other:
        # schools.append(s[0].text.encode('utf-8'))
    # students.append(other[1].find(text=True))
    # for t in other:
    #     students.append(s.text.encode('utf-8'))
    # minority.append(other[2].find(text=True))
    # for m in other:
    #     minority.append(s.text.encode('utf-8'))

# print schools
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
