from bs4 import BeautifulSoup
#includes ability to parse html, it can follow docment tree structure
import csv
# a csv file is essentialy a file with a very specific delimiter( , ), custom headers, to make rows in right format 
import re

#open the file (we use with clause to not lock my file)
with open('gv_50.html', 'r', encoding='utf-8') as HTML_file:
    soup = BeautifulSoup(HTML_file, 'html.parser')

    #find the parent tag for memorials
    memorials = soup.find_all('div', attrs = {"role": "group", "aria-label": "Memorial"})

    # List for results
    data = []

    for memorial in memorials:
        #small reminder that find method returns tag data rather than string so careful
        name_url = memorial.find('a').get('href')
        name_tag = memorial.find('i', class_= "pe-2")
        veteran_tag = memorial.find('span', title="Veteran")
        dates_tag = memorial.find('b', class_="birthDeathDates fw-light fs-5 text-body")
        location_tag = memorial.find('p', class_="addr-cemet mb-1") 

        # call functions and extract information
        name_details = extract_name_details(name_url, name_tag)
        birth, death = extract_dates(dates_tag)
        grave_location = extract_grave_location(location_tag)
        veteran_status = 'Y' if veteran_tag else ''
        
        data.append({

        })

    

# write data to csv file
with open('parsed_names.csv', 'w', newline='', encoding ="utf-16") as csv_file:
    #encoding utf-16 instead utf-8 because it gives more bytes(people with characters in the standard character set, like Korean, Japanese, emojis etc.)

    fieldnames = ['Memorial Id', 'Prefix', 'First Name', 'Middle Name', 'Maiden Name', 'Last Name', 'Suffix', 'Veteran', 'Birth Day', 'Birth Month', 'Birth Year', 'Death Day', 'Death Month', 'Death Year', 'Section', 'Lot']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)