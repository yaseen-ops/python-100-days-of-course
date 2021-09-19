from selenium import webdriver
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"


def price_affordable(item_ids):
    items_prices = []
    for item in item_ids:
        item_data = driver.find_element_by_id(item).text
        rate = int(item_data.split("\n")[0].split("-")[1].strip().replace(",", ""))
        items_prices.append(rate)
    items_prices.sort(reverse=True)
    get_money = driver.find_element_by_id("money").text
    if "," in get_money:
        current_balance = int(get_money.replace(",", ""))
    else:
        current_balance = int(get_money)
    for price in items_prices:
        if current_balance >= price:
            return price
    return


def item_to_buy(item_ids, item_price):
    for item in item_ids:
        item_data = driver.find_element_by_id(item).text
        rate = int(item_data.split("\n")[0].split("-")[1].strip().replace(",", ""))
        if rate == item_price:
            return item
    return


chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.implicitly_wait(10)

cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
item_ids_list = [item.get_attribute("id") for item in items]
item_ids_list.pop(-1)  # to remove the last item from the list, because of illogically extra item

timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    cookie.click()
    if time.time() > timeout:
        buy_price = price_affordable(item_ids=item_ids_list)
        item_buy_id = item_to_buy(item_ids=item_ids_list, item_price=buy_price)
        item_buy = driver.find_element_by_id(item_buy_id)
        item_buy.click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_sec = driver.find_element_by_id("cps").text
        print(cookies_per_sec)
        break

driver.quit()
