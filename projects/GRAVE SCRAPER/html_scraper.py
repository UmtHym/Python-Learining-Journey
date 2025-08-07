from bs4 import BeautifulSoup
#includes ability to parse html, it can follow document tree structure
import csv
# a csv file is essentialy a file with a very specific delimiter( , ), custom headers, to make rows in right format 
import re

def extract_name_details(name_url, name_tag):

    url_parts = name_url.split('/')
    #[,memorial,239660245, ruth-m-aaron]
    memorial_id = url_parts[2]
    name_parts = url_parts[3].split('-')
    name_parts = [name_part.title() for name_part in name_parts] #Capitalizes each word in the list 

    #For better readability, replacing underscores with spaces
    first_name = name_parts[0].replace('_', ' ') 
    last_name = name_parts[-1].replace('_', ' ')
    middle_name = name_parts[1].replace('_', ' ') if len(name_parts) == 3 else ''

    full_text = name_tag.get_text()# get_text gets also the text within the inner tags inside the tag we are parsing
    # name_tag example: <i class'"pe-2"> Vivian Starz <i>Pape</i> Backoff</i>
    prefix_tag = name_tag.find('span', class_='prefix')
    prefix = prefix_tag.get_text() if prefix_tag else ''
    #prefix = ''

    maiden_tag = name_tag.find('i')
    maiden_name = maiden_tag.get_text() if maiden_tag else ''
    #maiden = 'Pape'

    nickname_match = re.search(r'“([^”]+)”', full_text)
    nickname = nickname_match.group(1) if nickname_match else ''

    if nickname:
        first_name = f'{first_name} {nickname}' # this is called an 'fstring' (template literal in js)

    suffix = ''
    if full_text.split()[-1] in {"Jr.", "Sr.", "II", "III", "IV", "V", "MD"}:
        suffix = full_text.split()[-1]

    return {
        "Memorial ID": memorial_id,
        "Prefix": prefix,
        "First Name": first_name,
        "Middle Name": middle_name,
        "Maiden Name": maiden_name,
        "Last Name": last_name,
        "Suffix": suffix
    }

def parse_date(date_string):
    if date_string.lower() =='unknown':
        return {"day": None, "month": None, "year": 'unknown'}

    # 9 May 1997
    # [8,May,1997]
    parts = date_string.split()
    day = parts[0] if len(parts) == 3 else None
    month = parts[-2] if len(parts) >= 2 else None
    year = parts[-1] if len(parts) >= 1 else None
    return {"day": day, "month": month, "year": year}

def extract_dates(dates_tag):
    birth_date, death_date = None, None
    if dates_tag:
        dates_text = dates_tag.get_text().strip()
        # 3 Jul 1896 - 29 Dec 1964
        birth_date, death_date = map(str.strip, dates_text.split('–'))
        
    birth = parse_date(birth_date) if birth_date else {"day": None, "month": None, "year": "unknown"}
    death = parse_date(death_date) if death_date else  {"day": None, "month": None, "year": "unknown"}
    return birth, death
    
def extract_grave_location(location_tag):
    if location_tag:
        location_text = location_tag.find('strong').get_text().strip() if location_tag.find('strong') else ""
        section_match = re.search(r"(?:Sec(?:tion)?\s+)?([A-Za-z]+)", location_text, re.IGNORECASE)
        lot_match = re.search(r"(\d+)", location_text, re.IGNORECASE)
        section = section_match.group().split()[-1].upper() if section_match else ''
        lot = int(lot_match.group()) if lot_match else ''
        return {"Section": section, "Lot": lot}
    return {"Section": None, "Lot": None}


# Open the file (we use with clause to not lock my file)
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
           **name_details,
             # "**" allows us to unpack all the dictionary inside the name_details and match each of the values in the appropriate column in the return (if the format of my dictionary is the same format as my csv fields). Alttaki array 'fieldnames' csv filedaki columnlar, ve ** kullandigimizda eger format ve sira ayniysa direktman columnun altina valuelari yerlestiriyor.
           'Veteran': veteran_status,
           'Birth Day': birth['day'],
           'Birth Month': birth['month'],
           'Birth Year':birth['year'],
           'Death Day': death['day'],
           'Death Month': death['month'],
           'Death Year': death['year'],
           **grave_location
        })

    

# write data to csv file
with open('parsed_names.csv', 'w', newline='', encoding ="utf-16") as csv_file:
    #encoding utf-16 instead utf-8 because it gives more bytes(people with characters in the standard character set, like Korean, Japanese, emojis etc.)

    fieldnames = ['Memorial ID', 'Prefix', 'First Name', 'Middle Name', 'Maiden Name', 'Last Name', 'Suffix', 'Veteran', 'Birth Day', 'Birth Month', 'Birth Year', 'Death Day', 'Death Month', 'Death Year', 'Section', 'Lot']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print('Write Complete.')