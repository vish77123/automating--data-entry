from selenium import webdriver
import os
import time


def run():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get("https://cutt.ly/KWecMLq")
    time.sleep(30)
    name = driver.find_element_by_id("listing-type")
    print(name.text)



    driver.quit()

if __name__ == '__main__':
    run()