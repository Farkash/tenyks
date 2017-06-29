import urllib2
from bs4 import BeautifulSoup
import pandas
import csv

page1 = 'https://www.privateschoolreview.com/alabama'

alabama = urllib2.urlopen(page1)

soup = BeautifulSoup(alabama, "lxml")

target_divs = soup.find_all("div", class_="school-type-list-text")

counties = []
other_data = []
for div in target_divs:
    county = div.find_all("div", class_="table_cell_county")
    for c in county:
        counties.append(c.text.encode('utf-8'))
    other = div.find_all("div", class_="table_cell_other")
    for i in other:
        other_data.append(i.text.encode('utf-8'))



for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    states = row.findAll("th")
    if len(cells) == 6:
        A.append(cells[0].find(text = True))    
        B.append(states[0].find(text = True))
        C.append(cells[1].find(text = True))
        D.append(cells[2].find(text = True))
        E.append(cells[3].find(text = True))
        F.append(cells[4].find(text = True))
        G.append(cells[5].find(text = True))

df = pandas.DataFrame(A, columns = ['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G

# print other_data

# generate lists
# A = []
# B = []
# C = []
# D = []

# for div in target_divs:
    # county = div.find_all("div", class_= "table_cell_county")
    # other = div.find_all("div", class_= "table_cell_other")

    # A.append(county[0].find(text = True)) 
    # B.append(other[0].find(text = True))
    # C.append(other[1].find(text = True))
    # D.append(other[2].find(text = True))

df = pandas.DataFrame(counties, columns = ['County'])
df['Schools'] = other_data
df['Students'] = 
df['Minority'] = D

# print df

# df.to_csv("india-test.csv", encoding = 'utf-8')


