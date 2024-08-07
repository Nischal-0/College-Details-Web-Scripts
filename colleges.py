import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.shikshasanjal.com/top-plus-two-colleges-in-kathmandu")

soup =BeautifulSoup(req.content, "html.parser")

college_details = soup.find_all('div', class_='college-detail-content')

for details in college_details:
    
    name = details.find('h3', class_='college-name').get_text(strip = True)
    
    print(name)
    
    break

print(college_details)
# req.raise_for_status()          #throw an error if the website is not functional or error is detected
print(soup.get_text())



#stucture level of the HTML (inspect) page code

# body 
# section (class = colz-list-page)
# div class (class = container-fluid) 
# div class (class = row) 
# div class (class = col-sm-7) 
# div class (class = college-detail-content) 
# h3 (class = college-name)


