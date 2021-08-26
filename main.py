from selenium import webdriver
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
driver.get("https://cutt.ly/KWecMLq")
time.sleep(8)
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
    driver2.get("https://forms.gle/AwAeSnzQnMNCSXMM6")
    time.sleep(2)
    address = driver2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_selenium = driver2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_sele = driver2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address.send_keys(data[i]["addrs"])
    price_selenium.send_keys(data[i]["price"])
    link_sele.send_keys(data[i]["link"])
    submit.click()



driver.quit()
