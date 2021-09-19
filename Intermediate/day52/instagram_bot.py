from selenium import webdriver
from blahblah import get_secrets
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

EMAIL_ID = get_secrets().get("mail")["email_id"]
EMAIL_PASSWORD = get_secrets().get("mail")["email_password"]
URL = "https://www.instagram.com"
CELEB = "chef_pillai"
CHROME_DRIVER = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"


class InstallFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2)
        try:
            login = self.driver.find_element_by_class_name("ENC4C")
            login.click()
            time.sleep(2)
        except NoSuchElementException:
            pass
        email = self.driver.find_element_by_name("username")
        email.send_keys(EMAIL_ID)
        password = self.driver.find_element_by_name("password")
        password.send_keys(EMAIL_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        not_now = self.driver.find_element_by_css_selector(".cmbtv button")
        not_now.click()
        try:
            no_notification = self.driver.find_element_by_class_name("HoLwm")
            no_notification.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"{URL}/{CELEB}")
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstallFollower(CHROME_DRIVER)
bot.login()
bot.find_followers()
bot.follow()

# driver.quit()