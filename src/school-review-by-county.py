import urllib2
from bs4 import BeautifulSoup
import pandas

base_url = "https://www.privateschoolreview.com"

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
    url = base_url + "/" + st
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
        county_url = base_url + "/" + st + "/" + county[i].lower().replace(' ', '-')
        print county_url
        opened_county = urllib2.urlopen(county_url)
        county_soup = BeautifulSoup(opened_county, "lxml")
        target_school_text = county_soup.find_all("div", class_="school-type-list-text")
        for d in target_school_text:
            if d.find("a", href=True) != None:
                school_url = base_url + d.find("a", href=True)['href']
                print school_url
                opened_school = urllib2.urlopen(school_url)
                school_soup = BeautifulSoup(opened_school, "lxml")
                school_name = school_soup.find("h1", id="main-headline").text
                print school_name
                street_address = school_soup.find("span", itemprop="streetAddress").text
                print street_address
                city = school_soup.find("span", itemprop="addressLocality").text
                print city
                state = school_soup.find("span", itemprop="addressRegion").text
                print state 
                zipcode = school_soup.find("span", itemprop="postalCode").text
                print zipcode
                phone = school_soup.find("div", class_="top_card_ctn top_telephone_ctn").text
                phone = phone[(phone.find(' ')+1):len(phone)]
                print phone
                website = school_soup.find("a", class_="website_click")
                if website != None:
                    website = website.text
                print website
                details_table = school_soup.find("div", id="school_details_table")
                details_list = details_table.find_all("tr", id='school_membership_row')
                detail_list = filter(None, details_list)
                for e in range(0, len(details_list)):
                    details_list[e] = details_list[e].text.encode('utf-8')
                # print details_list
                for f in range(0, len(details_list)):
                    if "Grades Offered" in details_list[f]:
                        grades_raw_list = details_list[f].split('\n')
                        print "Grades offered: %s" % grades_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Total Students" in details_list[f]:
                        students_raw_list = details_list[f].split('\n')
                        print "Total Students: %s" % students_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Student Body Type" in details_list[f]:
                        body_type_raw_list = details_list[f].split('\n')
                        print "Student Body Type: %s" % body_type_raw_list[2]
                for f in range(0, len(details_list)):
                    if "% Students of Color" in details_list[f]:
                        minority_raw_list = details_list[f].split('\n')
                        print "Minority: %s" % minority_raw_list[2]        
                for f in range(0, len(details_list)):
                    if "Total Classroom Teachers" in details_list[f]:
                        teachers_raw_list = details_list[f].split('\n')
                        print "Teachers: %s" % teachers_raw_list[2]          
                for f in range(0, len(details_list)):
                    if "Student : Teacher Ratio" in details_list[f]:
                        stratio_raw_list = details_list[f].split('\n')
                        print "S:T Ratio: %s" % stratio_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Religious Affiliation" in details_list[f]:
                        religious_raw_list = details_list[f].split('\n')
                        print "Religious Affiliation: %s" % religious_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Year Founded" in details_list[f]:
                        founded_raw_list = details_list[f].split('\n')
                        print "Year Founded: %s" % founded_raw_list[2]
                for f in range(0, len(details_list)):
                    if "% Faculty w/Advanced Degree" in details_list[f]:
                        degree_raw_list = details_list[f].split('\n')
                        print "% Faculty w/Advanced Degree: %r" % degree_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Average Class Size" in details_list[f]:
                        size_raw_list = details_list[f].split('\n')
                        print "Average Class Size %s" % size_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Average ACT score" in details_list[f]:
                        act_raw_list = details_list[f].split('\n')
                        print "Average ACT score" % act_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Yearly Tuition Cost" in details_list[f]:
                        tuition_raw_list = details_list[f].split('\n')
                        print "Yearly Tuition Cost" % tuition_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Acceptance Rate" in details_list[f]:
                        acceptance_raw_list = details_list[f].split('\n')
                        print "Acceptance Rate" % acceptance_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Total Sports Offered" in details_list[f]:
                        sports_raw_list = details_list[f].split('\n')
                        print "Total Sports Offered" % sports_raw_list[2]
                for f in range(0, len(details_list)):
                    if "Total Extracurriculars" in details_list[f]:
                        extra_raw_list = details_list[f].split('\n')
                        print "Total Extracurriculars" % extra_raw_list[2]
                
        
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
