from pyvirtualdisplay import Display
from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

display = Display(visible=False, size=(800, 600))
display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.get("https://cutt.ly/KWecMLq")
time.sleep(100)
name = driver.find_element_by_id("listing-type")
print(name.text)



display.stop()

