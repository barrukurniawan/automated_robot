from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("youtube robot gaptek buat alat anti maling")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/g-section-with-header/div[2]/g-scrolling-carousel/div[1]/div/div/div[1]/g-inner-card/div/a/div[2]/div').click()
time.sleep(6)
driver.close()
print ("success running robot program")
