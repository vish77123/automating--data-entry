from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

wait = WebDriverWait(driver, 10)
driver.get("https://cutt.ly/KWecMLq")

soup = BeautifulSoup(driver.page_source, "html.parser")
price = soup.find_all(class_="list-card-price")
addrs = soup.find_all(class_="list-card-addr")
link = soup.select(".list-card-info a")
data =[]
dic = {}
for i in range (len(price)):
    href = link[i]["href"]
    if "http" not in href :
        href = f"https://www.zillow.com{href}"

    dic = {"price":price[i].text[:6],
           "addrs":addrs[i].text,

           "link":href
           }

    data.append(dic)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--no-sandbox")
driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


for i in range(len(data)):
    time.sleep(2)
    wait2 = WebDriverWait(driver2, 10)
    driver2.get("https://forms.gle/AwAeSnzQnMNCSXMM6")
    time.sleep(2)
    address = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_selenium = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_sele = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    submit = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    address.send_keys(data[i]["addrs"])
    price_selenium.send_keys(data[i]["price"])
    link_sele.send_keys(data[i]["link"])
    submit.click()




