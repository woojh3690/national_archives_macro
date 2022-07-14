#-*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from group_search_list import *

import csv

BASE_URL = "https://www.archives.go.kr/"
RESULT_DIR = "./result/{}. {}.csv"

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

def getListData(tab, startIdx, endIdx):
    form_xpath = '//*[@id="tab{}"]/div[2]/div[{}]/span[{}]'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        item = []
        for colIdx in [2, 1, 3]:
            cell_xpath = form_xpath.format(tab, idx + 1, colIdx)
            text = driver.find_element(By.XPATH, cell_xpath).text
            item.append(text)
            print(text, end='  |  ')
        print('')
        items.append(item)
    return items

def countKeyWord(keyword, items):
    cText = '{}({})'
    for idx, item in enumerate(items):
        count = item[2].count(keyword)
        items[idx].insert(2, cText.format(keyword, count))

def writeCsv(keyword_idx, keyword, items):
    with open(RESULT_DIR.format(keyword_idx, keyword), 'w', encoding='utf-8-sig', newline='') as f:
        rdr = csv.writer(f, delimiter=',')
        for item in items:
            rdr.writerow(item)

if __name__ == '__main__':
    driver = init_driver()
    wait = WebDriverWait(driver, 30)

    for keyword_idx, keyword in enumerate(search_list):
        driver.get(BASE_URL + 'next/search/viewDescClassMain.do')
        keyWordBox = driver.find_element(By.XPATH, '//*[@id="kindword"]')
        keyWordBox.send_keys(keyword)
        keyWordBox.send_keys(Keys.ENTER)

        allItems = []
        for tabId in [1, 2]:
            btn_xpath = '//*[@id="defaultOpen{}"]'.format(tabId)
            elementMaxIdx = driver.find_element(By.XPATH, btn_xpath)

            # 조회 건수 가져오기
            s = elementMaxIdx.text
            s = s[s.find("(")+1:s.find(")")]
            maxIdx = int(s.replace(',',''))
            print("조회 건수:", maxIdx)

            elementMaxIdx.click()

            items = []
            if (maxIdx > 10):
                # 첫 페이지
                items = items + getListData(tabId, 0, 5)

                # 마지막 페이지
                page = int(maxIdx / 10)
                remain = maxIdx % 10
                btn_page = '//*[@id="tab{}"]/div[3]/ul/li/div/ul/a[{}]'
                driver.find_element(By.XPATH, btn_page.format(tabId, 'last()')).click()
                
                if (remain >= 5):
                    items = items + getListData(tabId, remain - 5, remain)
                elif (remain == 0):
                    items = items + getListData(tabId, 5, 10)
                else:
                    lastItems = getListData(tabId, 0, remain)
                    driver.find_element(By.XPATH, btn_page.format(tabId, 2)).click()
                    items = items + getListData(tabId, 5 + remain, 10)
                    items = items + lastItems
            elif (maxIdx > 0):
                items = items + getListData(tabId, 0, maxIdx)
            else:
                print("검색 결과 없음")
            countKeyWord(keyword, items)
            allItems = allItems + items
        writeCsv(keyword_idx, keyword, allItems)