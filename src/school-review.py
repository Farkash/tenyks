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
other = []
schools = []
students = []
minority = []


# since target_divs is a list of divs, we need to loop over each item to 
# perform any functions on the entire list
for div in target_divs:
    county.append(div.find("div", class_="table_cell_county"))

county = filter(None, county)  # get rid of empty divs
for i in range(0, len(county)):  # overwrite county data with just the text
    county[i] = county[i].text

# use a loop to populate the 'other' list
for div in target_divs:
    other.append(div.find_all("div", class_="table_cell_other"))

other = filter(None, other)
for each in other:
    schools.append(each[0].text.encode('utf-8'))
    students.append(each[1].text.encode('utf-8'))
    minority.append(each[2].text.encode('utf-8'))

# print schools
# print students
# print minority

# string manip. Clean out "County", "Schools", "Students", and "Minority". Also convert minority to decimal
# remove everything after the first space
# 1. find the first space
# 2. slice out everything after the first space
# Something like county[0][0:find(' ')]
print county[0][0:find(' ')]

# df = pandas.DataFrame(county, columns=['County'])
# df['Schools'] = schools
# df['Students'] = students
# df['Minority'] = minority

# print df

# df.to_csv("/Users/Steve/Dropbox/tenyks/data/alabama_county_info.csv", encoding ='utf-8', index=False)
