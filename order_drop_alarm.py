import requests
import time
from bs4 import BeautifulSoup
order_url = "https://orderscount.apps.cfcommerce.prod.azeus.gaptech.com/relative_order_count/?relative_time_in_minutes=2&synthetic_included=N&NGCC_included=N"


def check_order_drop():
    response = requests.get(order_url)
    response_text = response.text
    soup = BeautifulSoup(response_text, features='html.parser')
    # print(soup.prettify())
    # print(soup.title.text)

    # make a list of all <td> elements (data cells)
    cell_list = list(soup.find_all("td"))
    cell_13 = cell_list[13]
    cell_27 = cell_list[27]
    orders_2min_ago = [int(x) for x in cell_13 if x.isdigit()]
    orders_1min_ago = [int(x) for x in cell_27 if x.isdigit()]
    order_diff = orders_1min_ago[0] - orders_2min_ago[0]
    drop_percent = 100 * order_diff / orders_2min_ago[0]
    return orders_2min_ago, orders_1min_ago, drop_percent


while True:
    before, after, drop = check_order_drop()
    if drop != :
        print(before, after, drop)
        print("order drop more than 15%")
    else:
        print(before, after, drop)
    time.sleep(60)