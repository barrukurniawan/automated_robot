from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("youtube robot gaptek buat alat anti maling")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="_JGezXuzBEM6w9QPCwKKIBA18"]/div[1]/div/div/div[1]/g-inner-card/div/a/div[2]/div').click()
time.sleep(6)
driver.close()
print ("success running robot program")
