from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()