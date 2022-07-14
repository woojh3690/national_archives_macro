#-*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from group_search_list import *

import time
import csv

BASE_URL = "https://www.archives.go.kr/"

def init_driver():
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    # options.add_argument('--remote-debugging-port=9222')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    return driver

#def getListData(driver):


if __name__ == '__main__':
    driver = init_driver()
    wait = WebDriverWait(driver, 30)

    for keyword in search_list:
        driver.get(BASE_URL + 'next/search/viewDescClassMain.do')
        keyWordBox = driver.find_element(By.XPATH, '//*[@id="kindword"]')
        keyWordBox.send_keys(keyword)
        keyWordBox.send_keys(Keys.ENTER)

        for idx in [1, 2]:
            elementMaxIdx = driver.find_element(By.XPATH, 
                '//*[@id="defaultOpen{}"]'.format(idx)
            ).click()

            elementMaxIdx = driver.find_element(By.XPATH, 
                '//*[@id="defaultOpen{}"]'.format(idx)
            )

            # 전체 조회 건수 가져오기
            s = elementMaxIdx.text
            s = s[s.find("(")+1:s.find(")")]
            maxIdx = int(s.replace(',',''))
            print("조회 건수:", maxIdx)
            time.sleep(5)