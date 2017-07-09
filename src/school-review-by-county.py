import urllib2
from bs4 import BeautifulSoup
import pandas

base_url = "https://www.privateschoolreview.com/"

state_list = ["alabama"
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
            #   "west-virginia", "wisconsin", "wyoming"
              ]
# declare lists
county = []
county_short = []
state = []

    
big_frame = pandas.DataFrame(columns=['State', 'County'])

for st in state_list:
    url = base_url + st
    opened_state = urllib2.urlopen(url)
    soup = BeautifulSoup(opened_state, "lxml")

# soup is one object here, not a list of objects, so we
# can apply the find_all function to it once. Don't need to loop at all
    target_divs = soup.find_all("div", class_="school-type-list-text")

    # since target_divs is a list of divs, we need to loop over each item to
    # perform any functions on the entire list
    for div in target_divs:
        county.append(div.find("div", class_="table_cell_county"))

    county = filter(None, county)  # get rid of empty divs
    for i in range(0, len(county)):  # overwrite county data with just the text
        county[i] = county[i].text.encode('utf-8')
        # insert hyphen and lower county name and assemble county URL:
        # grep?
        county_url = base_url + st + "/" + county[i].lower().replace(' ', '-')
        print county_url
        opened_county = urllib2.urlopen(county_url)
        county_soup = BeautifulSoup(opened_county, "lxml")
        target_school_text = county_soup.find_all("div", class_="school-type-list-text")
        school_url = []
        for d in target_school_text:
            if d.find("a", href=True) != None:
                school_url.append(d.find("a", href=True)['href'])
                print school_url
        
        
        
        # county_short[i] = county[i][0:county[i].find(' ')]

# grab the school detail within each county
    

    # use a loop to populate the 'other' list
    for div in target_divs:
        other.append(div.find_all("div", class_="table_cell_other"))

    other = filter(None, other)
    for each in other:
        schools.append(each[0].text.encode('utf-8'))
        students.append(each[1].text.encode('utf-8'))
        minority.append(each[2].text.encode('utf-8'))
        state.append(st.title())

    


    df = pandas.DataFrame(columns=['State', 'County')
    df['State'] = state
    df['County'] = county
    
    big_frame = big_frame.append(df, ignore_index=True)

# print big_frame

# write final frame of all states out to csv
# big_frame.to_csv("/Users/Steve/Dropbox/tenyks/data/state_summary.csv",
#                  encoding='utf-8', index=False)
