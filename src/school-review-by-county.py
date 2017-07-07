# school-level data
# assemble list of URLs from the state_list and the county list. 
# Don't care about county-level stuff anymore like number of schools
# or students or %minority. 
# In this set, find state, county, school, address, phone,
# grades taught, students
# from school-level page: website, fact list, school memberships,
# student body type, % students of color, total classroom teachers,
# student:teacher ratio

# how do I make a list of lists of lists? 
# for each state, I want a list of counties in it
# for each county, I want a list of schools in it

# You want to create an empty list, then append the created list to it. 
# This will give you the list of lists. Example:
# l = []
# l.append([1,2,3])
# l.append([4,5,6])
# l
# [[1, 2, 3], [4, 5, 6]]

#also add in the URLs for each school's page so users can navigate there

# make URLs like this: 
# https://www.privateschoolreview.com/alabama/autauga-county

# page to get even more detail
# https://www.privateschoolreview.com/autauga-academy-profile

import urllib2
from bs4 import BeautifulSoup
import pandas

# make a list of links, one per state
# loop through the list applying all below
# make sure to add a state field based off the current state
# append result frame from each state to master frame

master_list = ["alabama"
# , "alaska",
#               "arizona", "arkansas",
#               "california", "colorado",
#               "connecticut", "delaware", "district-of-columbia",
#               "florida", "georgia", "hawaii",
#               "idaho", "illinois", "indiana", "iowa", "kansas",
#               "kentucky", "louisiana",
#               "maine", "maryland", "massachusetts", "michigan",
#               "minnesota", "mississippi",
#               "missouri", "montana", "nebraska", "nevada",
#               "new-hampshire", "new-jersey",
#               "new-mexico", "new-york", "north-carolina",
#               "north-dakota", "ohio", "oklahoma",
#               "oregon", "pennsylvania", "rhode-island",
#               "south-carolina", "south-dakota",
#               "tennessee", "texas", "utah", "vermont",
#               "virginia", "washington",
#               "west-virginia", "wisconsin", "wyoming"
              ]

# big_frame = pandas.DataFrame(columns=['State', 'County', 'Schools',
#                                       'Students', 'Minority'])

# I need to open up each state's page and scrape for counties
for item in master_list:
    url = 'https://www.privateschoolreview.com/%s' % item
    item_blob = urllib2.urlopen(url)
    soup = BeautifulSoup(item_blob, "lxml")
    
    target_divs = soup.find_all("div", class_="school-type-list-text")
 
    for div in target_divs:
        county.append(div.find("div", class_="table_cell_county"))
    
    county = filter(None, county)  # get rid of empty divs

    for i in range(0, len(county)):  # overwrite county data with just the text
        county[i] = county[i].text.encode('utf-8')
        # county[i] = county[i][0:county[i].find(' ')]
        
    master_list.append(county)









# soup is one object here, not a list of objects, so we
# can apply the find_all function to it once. Don't need to loop at all
    target_divs = soup.find_all("div", class_="school-type-list-text")

    # declare lists
    county = []
    state = []
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



    # use a loop to populate the 'other' list
#     for div in target_divs:
#         other.append(div.find_all("div", class_="table_cell_other"))

#     other = filter(None, other)
#     for each in other:
#         schools.append(each[0].text.encode('utf-8'))
#         students.append(each[1].text.encode('utf-8'))
#         minority.append(each[2].text.encode('utf-8'))
#         state.append(st.title())

#     for i in range(0, len(schools)):
#         schools[i] = schools[i][0:schools[i].find(' ')]

#     for i in range(0, len(students)):
#         students[i] = students[i][0:students[i].find(' ')]
#         students[i] = students[i].replace(',', '')

#     for i in range(0, len(minority)):
#         minority[i] = minority[i][0:minority[i].find('%')]
#         if minority[i][0] == '-':
#             minority[i] = ''
#         if minority[i] != '':
#             minority[i] = float(minority[i]) / 100

#     # print schools
#     # print students
#     # print minority

#     df = pandas.DataFrame(columns=['State', 'County', 'Schools',
#                                   'Students', 'Minority'])
#     df['State'] = state
#     df['County'] = county
#     df['Schools'] = schools
#     df['Students'] = students
#     df['Minority'] = minority

#     big_frame = big_frame.append(df, ignore_index=True)

# # print big_frame

# # write final frame of all states out to csv
# big_frame.to_csv("/Users/Steve/Dropbox/tenyks/data/state_summary.csv",
#                  encoding='utf-8', index=False)
