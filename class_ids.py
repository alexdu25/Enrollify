from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://sa.ucla.edu/ro/public/soc")
print(driver.title)
print(driver.current_url)

# text_field = driver.find_element_by_name('q')
# text_field.send_keys('python selenium')
# text_field.submit()

# dropdown = Select(driver.find_element(By.CLASS_NAME, "select_filter_term"))
# dropdown.select_by_value('23S')
time.sleep(1500)



# driver.close()
#select_filter_term