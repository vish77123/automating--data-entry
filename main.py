import requests
from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

responce = requests.get(url="https://ysense.com/")
data = responce.text
soup = BeautifulSoup(data, "html.parser")
time.sleep(30)
name = soup.find(class_="login")
print(name.text)





