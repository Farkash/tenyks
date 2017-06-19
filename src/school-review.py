import urllib2
from bs4 import BeautifulSoup
import pandas
import csv

page1 = 'https://www.privateschoolreview.com/alabama'

alabama = urllib2.urlopen(page1)

soup = BeautifulSoup(alabama, "lxml")

# print soup.prettify()

# print soup.title.string

target_divs = soup.find_all("div", class_= "school-type-list-text")
for div in target_divs:
    county = div.find_all("div", class_= "table_cell_county")
    for div in county:
        print div.text
    other = div.find_all("div", class_="table_cell_other")
    for div in other:
        print div.text

# county = target_divs.find_all("div", class_= "table_cell_county")

# other = target_divs.find_all("div", class_="table_cell_other")


# list1 = ["this", "is", "dumb"]
# print list1[0]

# print target_divs[0]

# print county[0]

# print county.index('<div class="table_cell_county"><a href="/alabama/autauga-county">Autauga County</a></div>')

# for div in target_divs:
#     print div

# generate lists
# A = []
# B = []
# C = []
# D = []
# # E = []
# # F = []

# for div in target_divs:
    # county = div.find_all("div", class_= "table_cell_county")
    # other = div.find_all("div", class_= "table_cell_other")

    # A.append(county[0].find(text = True))	
    # B.append(other[0].find(text = True))
    # C.append(other[1].find(text = True))
    # D.append(other[2].find(text = True))

# df = pandas.DataFrame(A, columns = ['County'])
# df[''] = B
# df['Schools'] = C
# df['Students'] = D
# df['Minority'] = E

# print df

# df.to_csv("india-test.csv", encoding = 'utf-8')


