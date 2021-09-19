from selenium import webdriver

URL = "https://www.python.org"

chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
events_time = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}
for n in range(len(events_time)):
    events[n] = {
        "time": events_time[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()