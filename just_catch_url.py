from bs4 import BeautifulSoup
from urllib3 import urlopen3
order_url = "https://orderscount.apps.cfcommerce.prod.azeus.gaptech.com/relative_order_count/?relative_time_in_minutes=2&synthetic_included=N&NGCC_included=N"

html = urlopen('' + order_url)
soup = BeautifulSoup(html.read(), 'lxml')
names = soup.findAll("td", {"class": "main"})
salary = soup.findAll("td", {"class": "td"})
print(salary)
