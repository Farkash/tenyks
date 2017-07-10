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

state_full_final = []
county_final = []
county_short_final = []
school_name_final = []
street_final = []
city_final = []
state_final = []
zip_code_final = []
phone_final = []
website_final = []
psr_webpage_final = []
grades_final = []
total_students_final = []
student_body_final = []
minority_final = []
teachers_final = []
s_t_ratio_final =[]
religion_final = []
year_founded_final = []
faculty_degree_final = []
class_size_final = []
act_final = []
tuition_final = []
acceptance_final = []
sports_final = []
extra_final = []
    
big_frame = pandas.DataFrame(columns=['State Full', 'County', 'School Name', 'Street Address',
'City', 'State', 'Zip Code', 'Phone Number', 'Website', 'Grades Offered', 
'Total Students', 'Student Body Type', 'Students of Color Percentage', 
'Total Classroom Teachers', 'Student-Teacher Ratio', 'Religious Affiliation', 
'Year Founded', 'Faculty with Advanced Degree Percentage', 'Average Class Size',
'Average ACT Score', 'Yearly Tuition Cost', 'Acceptance Rate', 'Total Sports Offered',
'Total Extracurriculars'])

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
                psr_webpage.append(school_url)
                state_full.append(st)
                county_main.append(county)
                opened_school = urllib2.urlopen(school_url)
                school_soup = BeautifulSoup(opened_school, "lxml")
                school_name = school_soup.find("h1", id="main-headline").text
                print school_name
                school_name.append(school_name)
                street_address = school_soup.find("span", itemprop="streetAddress").text
                print street_address
                city = school_soup.find("span", itemprop="addressLocality").text
                print city
                state_short = school_soup.find("span", itemprop="addressRegion").text
                print state_short
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
                        print "Grades offered: %r" % grades_raw_list[2]
                        print grades_raw_list
                for f in range(0, len(details_list)):
                    if "Total Students" in details_list[f]:
                        students_raw_list = details_list[f].split('\n')
                        print "Total Students: %r" % students_raw_list[2]
                        print students_raw_list
                for f in range(0, len(details_list)):
                    if "Student Body Type" in details_list[f]:
                        body_type_raw_list = details_list[f].split('\n')
                        print "Student Body Type: %r" % body_type_raw_list[2]
                        print body_type_raw_list
                for f in range(0, len(details_list)):
                    if "% Students of Color" in details_list[f]:
                        minority_raw_list = details_list[f].split('\n')
                        print "Minority: %r" % minority_raw_list[5]        
                        print minority_raw_list
                for f in range(0, len(details_list)):
                    if "Total Classroom Teachers" in details_list[f]:
                        teachers_raw_list = details_list[f].split('\n')
                        print "Teachers: %r" % teachers_raw_list[2]          
                        print teachers_raw_list
                for f in range(0, len(details_list)):
                    if "Student : Teacher Ratio" in details_list[f]:
                        stratio_raw_list = details_list[f].split('\n')
                        print "S:T Ratio: %r" % stratio_raw_list[2][0:stratio_raw_list[2].find('N')]
                        print stratio_raw_list
                for f in range(0, len(details_list)):
                    if "Religious Affiliation" in details_list[f]:
                        religious_raw_list = details_list[f].split('\n')
                        print "Religious Affiliation: %r" % religious_raw_list[2]
                        print religious_raw_list
                for f in range(0, len(details_list)):
                    if "Year Founded" in details_list[f]:
                        founded_raw_list = details_list[f].split('\n')
                        print "Year Founded: %r" % founded_raw_list[2]
                        print founded_raw_list
                for f in range(0, len(details_list)):
                    if "Faculty w/Advanced Degree" in details_list[f]:
                        degree_raw_list = details_list[f].split('\n')
                        print "Faculty w/Advanced Degree: %r" % degree_raw_list[5]
                        print degree_raw_list
                for f in range(0, len(details_list)):
                    if "Average Class Size" in details_list[f]:
                        size_raw_list = details_list[f].split('\n')
                        print "Average Class Size: %r" % size_raw_list[2]
                        print size_raw_list
                for f in range(0, len(details_list)):
                    if "Average ACT score" in details_list[f]:
                        act_raw_list = details_list[f].split('\n')
                        print "Average ACT score: %r" % act_raw_list[2]
                        print act_raw_list
                for f in range(0, len(details_list)):
                    if "Yearly Tuition Cost" in details_list[f]:
                        tuition_raw_list = details_list[f].split('\n')
                        print "Yearly Tuition Cost: %r" % tuition_raw_list[2][0:tuition_raw_list[2].find('V')]
                        print tuition_raw_list
                for f in range(0, len(details_list)):
                    if "Acceptance Rate" in details_list[f]:
                        acceptance_raw_list = details_list[f].split('\n')
                        print "Acceptance Rate: %r" % acceptance_raw_list[5]
                        print acceptance_raw_list
                for f in range(0, len(details_list)):
                    if "Total Sports Offered" in details_list[f]:
                        sports_raw_list = details_list[f].split('\n')
                        print "Total Sports Offered: %r" % sports_raw_list[2]
                        print sports_raw_list
                for f in range(0, len(details_list)):
                    if "Total Extracurriculars" in details_list[f]:
                        extra_raw_list = details_list[f].split('\n')
                        print "Total Extracurriculars: %r" % extra_raw_list[2]
                        print extra_raw_list
                
        


    


    df = pandas.DataFrame(columns=['State', 'County')
    df['State'] = state
    df['County'] = county
    
    big_frame = big_frame.append(df, ignore_index=True)

# print big_frame

# write final frame of all states out to csv
# big_frame.to_csv("/Users/Steve/Dropbox/tenyks/data/state_summary.csv",
#                  encoding='utf-8', index=False)
