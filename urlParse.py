import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the table
url = 'URL_OF_THE_WEBPAGE'

# Fetch the webpage content
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
table = soup.find('table')

# Initialize lists to store data
data_row2 = []
data_row3 = []

# Find rows containing "app ID" and "software name" in column 1
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1 and "app ID" in cells[0].text.lower():
        data_row2 = [cell.text for cell in cells]
    elif len(cells) > 1 and "software name" in cells[0].text.lower():
        data_row3 = [cell.text for cell in cells]

# Display the data
print("Data from Row with 'app ID':")
print(data_row2)

print("\nData from Row with 'software name':")
print(data_row3)