from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

#command to run in terminal from project directory
#  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --enable-logging --v=1 --remote-debugging-port=8989 --user-data-dir=chromeUserProfile

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(options=opt)
driver.switch_to.window(driver.window_handles[0])


get_url = driver.current_url
print("The current url is:"+str(get_url))

action = ActionChains(driver)

element = driver.find_element(By.ID, "ctl00_signInLink")

# click the item
action.click(on_element=element)

action.perform()
sleep(2)
action.send_keys(Keys.ENTER)
action.perform()
sleep(9)

for i in range(9):
    action.send_keys(Keys.TAB)
    action.perform()
action.send_keys(Keys.ENTER)
action.perform()
sleep(0.5)
for i in range(8):
    action.send_keys(Keys.TAB)
    action.perform()
action.send_keys(Keys.ENTER)
action.perform()

# Currently on class planner page

select = Select(driver.find_element(By.ID, 'ctl00_MainContent_cs_searchBy'))
select.select_by_value('classidnumber')
sleep(1.5)
textbox = driver.find_element(By.ID, "searchTier0")
textbox.send_keys("236003201")
sleep(1.5)
go_button = driver.find_element(By.ID, "ctl00_MainContent_cs_goButton")

action.click(on_element=go_button)
action.perform()
sleep(2)
#opens up class - cb_course_M0_236003201
check_box = driver.find_element(By.ID, "cb_course_M0_236003201")

action.click(on_element=check_box)
action.perform()

sleep(3)

enroll_button = driver.find_element(By.CLASS_NAME, "button.button_flyout_enroll")
action.click(on_element=enroll_button)
action.perform()

sleep(4)


elements = driver.find_elements(By.NAME, "confCheck")

for c_box in elements:
    action.click(on_element=c_box)
    action.perform()

enroll_button = driver.find_element(By.CLASS_NAME, "button.button_flyout_enroll")
action.click(on_element=enroll_button)
action.perform()


#236003201