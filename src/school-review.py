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
    county[i] = county[i].text.encode('utf-8')
    county[i] = county[i][0:county[i].find(' ')]

# print county

# use a loop to populate the 'other' list
for div in target_divs:
    other.append(div.find_all("div", class_="table_cell_other"))

other = filter(None, other)
for each in other:
    schools.append(each[0].text.encode('utf-8'))
    students.append(each[1].text.encode('utf-8'))
    minority.append(each[2].text.encode('utf-8'))

# print len(schools)
# schools = filter(None, schools)  # get rid of empty divs
# print len(schools)
for i in range(0, len(schools)):
    schools[i] = schools[i][0:schools[i].find(' ')]

for i in range(0, len(students)):
    students[i] = students[i][0:students[i].find(' ')]
    students[i] = students[i].replace(',', '')

for i in range(0, len(minority)):
    minority[i] = minority[i][0:minority[i].find('%')]
    if minority[i][0] == '-':
        minority[i] = ''
    if minority[i] != '':
        minority[i] = float(minority[i]) / 100

# print schools
# print students
# print minority

df = pandas.DataFrame(county, columns=['County'])
df['Schools'] = schools
df['Students'] = students
df['Minority'] = minority

# print df

df.to_csv("/Users/Steve/Dropbox/tenyks/data/alabama_county_info.csv", encoding ='utf-8', index=False)
