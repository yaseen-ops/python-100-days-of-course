from selenium import webdriver

URL = "https://www.amazon.in/Faddish-Anti-glare-Spectacle-Bluelight-HOOP/dp/B08J3VL7M6?pd_rd_w=BMgtc&pf_rd_p=218e88e6" \
      "-02df-4531-b5e1-61aaeb78a7f5&pf_rd_r=HBE02VY2FWXCNST3BNYQ&pd_rd_r=ab816c76-806b-47a0-b1b1-583ac806bd8f" \
      "&pd_rd_wg=RchCu&pd_rd_i=B08J3VL7M6&psc=1&ref_=pd_bap_d_rp_8_t"

chrome_driver_path = "C:/Users/yaseen/PycharmProjects/python-100-days-of-course/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
try:
    product_price = driver.find_element_by_id("priceblock_ourprice")
except:
    product_price = driver.find_element_by_id("priceblock_dealprice")
print(product_price.text)

# Examples
driver.get("https://www.python.org")
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

bug_fix_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_fix_link.text)
# close only closes the active TAB
# driver.close()
# quit closes the entire browser
driver.quit()
