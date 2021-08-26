import requests
from selenium import webdriver
import os
import time
#from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


time.sleep(12)
name = driver.find_element_by_class_name("signupFormTitle")
print(name.text)





