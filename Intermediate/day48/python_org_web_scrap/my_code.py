from selenium import webdriver

URL = "https://www.python.org"

chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
events = driver.find_elements_by_class_name("event-widget li")
events_list = [event.text for event in events]
new_list = [event.split("\n") for event in events_list]
events_dict = {key: value for (key, value) in new_list}
print(events_dict)

driver.quit()