from selenium import webdriver

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.implicitly_wait(10)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Logan")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Wolverine")
email = driver.find_element_by_name("email")
email.send_keys("dummy@gmail.com")
submit = driver.find_element_by_css_selector("form button")
submit.click()

#### OR ####

# f_name = driver.find_element_by_xpath("/html/body/form/input[1]")
# f_name.send_keys("Logan")
# l_name = driver.find_element_by_xpath("/html/body/form/input[2]")
# l_name.send_keys("Wolverine")
# email = driver.find_element_by_xpath("/html/body/form/input[3]")
# email.send_keys("dummy@gmail.com")
# submit = driver.find_element_by_xpath("/html/body/form/button")
# submit.click()
