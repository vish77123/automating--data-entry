from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

wait = WebDriverWait(driver, 10)
driver.get("https://ysense.com/")

login = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login")))
login.click()
time.sleep(5)
username= wait.until(EC.presence_of_element_located((By.ID, "username")))
password= wait.until(EC.presence_of_element_located((By.ID, "password")))
sign_in= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginform"]/div[6]/button')))
print(username)
print(password)
print(sign_in)
username.click()
username.send_keys("raghavmidtown68@gmail.com")
password.click()
password.send_keys("e99#yn,.")
sign_in.click()
time.sleep(10)
lifetime = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-details"]/table/tbody/tr[6]/td[2]/span')))
print(lifetime.text)
# price = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "list-card-price")))
# addrs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "list-card-addr")))
# link = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".list-card-info a")))
# data =[]
# dic = {}
# for i in range (len(price)):
#     href = link[i].get_attribute('href')
#     if "http" not in href :
#         href = f"https://www.zillow.com{href}"
#
#     dic = {"price":price[i].text[:6],
#            "addrs":addrs[i].text,
#
#            "link":href
#            }
#
#     data.append(dic)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--no-sandbox")
# driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#
#
# for i in range(len(data)):
#     time.sleep(2)
#     wait2 = WebDriverWait(driver2, 10)
#     driver2.get("https://forms.gle/AwAeSnzQnMNCSXMM6")
#     time.sleep(2)
#     address = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
#     price_selenium = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
#     link_sele = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
#     submit = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
#     address.send_keys(data[i]["addrs"])
#     price_selenium.send_keys(data[i]["price"])
#     link_sele.send_keys(data[i]["link"])
#     submit.click()




