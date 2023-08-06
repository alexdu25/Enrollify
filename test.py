from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
url = f'https://sa.ucla.edu/ro/public/soc/Results?SubjectAreaName=Mathematics+(MATH)&t=23S&sBy=subject&subj=MATH+++&catlg=&cls_no=&undefined=Go&btnIsInIndex=btn_inIndex'


try:
        # create a new instance of the Chrome driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        driver.implicitly_wait(10)
        eles=driver.execute_script('return document.querySelector("ucla-sa-soc-app").shadowRoot.querySelectorAll("*.demo1")[1].querySelectorAll("button")')
        driver.implicitly_wait(10)

        buttonsC=len(eles)

        for button in range(1,buttonsC-2):
            if button !=1:
                eles=driver.execute_script('return document.querySelector("ucla-sa-soc-app").shadowRoot.querySelectorAll("*.demo1")[1].querySelectorAll("button")')
                ele=eles[button]
                assert(ele.get_attribute("className") == '')
                driver.implicitly_wait(10)
                ele.click()
            driver.implicitly_wait(10)
            time.sleep(1)
            class_eles=driver.execute_script('return document.querySelector("ucla-sa-soc-app").shadowRoot.querySelectorAll("*.row-fluid.class-title")')
            curr_ids =[]
            for div in class_eles:
                curr_ids.append(div.get_attribute('id'))
            driver.implicitly_wait(10)
            expand_all_button = driver.execute_script('return document.querySelector("ucla-sa-soc-app").shadowRoot.getElementById("expandAll")')
            if expand_all_button is None:
                continue
            expand_all_button.click()
            driver.implicitly_wait(10)
            time.sleep(1)
            for class_id in curr_ids:
                ele=driver.execute_script(f'return document.querySelector("ucla-sa-soc-app").shadowRoot.getElementById("{class_id}-children")')
                driver.implicitly_wait(10)
                if ele is not None:
                    child_div = ele.find_element(By.XPATH, "./div")
                    print(child_div.get_attribute("id"))
            driver.implicitly_wait(10)
except:
        raise Exception("Something broke")