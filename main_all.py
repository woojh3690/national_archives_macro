#-*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_list_data import *
from search_list import *

import csv

BASE_URL = "https://www.archives.go.kr/"

# 관보, 피해자명부, 독립운동, 건축도면 판결문 안함
# "관보": '//*[@id="defaultOpen-original4"]',
# "독립운동 판결문": '//*[@id="defaultOpen-original7"]',
# "일제강점기 피해자명부": '//*[@id="defaultOpen-original8"]',
# "일제강점기 건축도면": '//*[@id="defaultOpen-original9"]',

dicSearchOpts = {
    "기본검색": '//*[@id="defaultOpen-original1"]',
    "공공누리": '//*[@id="defaultOpen-original2"]',
    "토지기록물": '//*[@id="defaultOpen-original3"]',
    "국무회의록": '//*[@id="defaultOpen-original5"]',
    "정부간행물": '//*[@id="defaultOpen-original6"]',
    "일제강점기 기록물": '//*[@id="defaultOpen-original10"]',
}

dicSearchBox = {
    "기본검색": '//*[@id="defaultKeyword1"]',
    "공공누리": '//*[@id="defaultKeyword2"]',
    "토지기록물": '//*[@id="acreageKeyword"]',
    "관보": '//*[@id="gazetteKeyword"]',
    "국무회의록": '//*[@id="cabinetKeyword"]',
    "정부간행물": '//*[@id="publishmentKeyword"]',
    "독립운동 판결문": '//*[@id="indyKeyword"]',
    "일제강점기 피해자명부": '//*[@id="japaneseKeyword"]',
    "일제강점기 건축도면": '//*[@id="planKeyword"]',
    "일제강점기 기록물": '//*[@id="governmentKeyword"]',
}

def init_driver():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    # options.add_argument('--remote-debugging-port=9222')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    return driver


def waitForSearch():
    wait.until(EC.invisibility_of_element((By.XPATH, '//*[@id="main"]/div[1]')))

def writeCsv(type, searchWd, items):
    with open(type + '_' + searchWd + '.csv', 'w', encoding='utf-8-sig', newline='') as f:
        rdr = csv.writer(f, delimiter=',')
        for item in items:
            rdr.writerow(item)

def getListData(type, page, startIdx = 0, endIdx = 5):
    waitForSearch()
    if (type=='관보'):
        return parse_gazette(driver, page, startIdx, endIdx)
    elif (type == '국무회의록'):
        return parse_proceedings(driver, page, startIdx, endIdx)
    elif (type == '일제강점기 기록물'):
        return parse_record(driver, page, startIdx, endIdx)
    else:
        return parse_default(driver, page, startIdx, endIdx)

if __name__ == '__main__':   
    """
        \"단어\"  단어1
        \"단 어\" 단어2
        단|어     단-어
        단*어     단0어
    """
    driver = init_driver()
    wait = WebDriverWait(driver, 30)

    for searchWd, fileName in searchKeyWords.items():
        driver.get(BASE_URL)

        for type, xpath in dicSearchOpts.items():
            # 검색
            driver.find_element(By.XPATH, '//*[@id="label_modal_2"]').click()
            driver.find_element(By.XPATH, xpath).click()
            keyWordBox = driver.find_element(By.XPATH, dicSearchBox[type])
            keyWordBox.click()
            keyWordBox.send_keys(searchWd)
            keyWordBox.send_keys(Keys.ENTER)

            elementMaxIdx = driver.find_element(By.XPATH, '//*[@id="depth1"]/div/a')

            # 전체 조회 건수 가져오기
            maxIdx = int(elementMaxIdx.text.replace(',','')[4:-1])
            print(type + " 조회 건수: ", maxIdx)

            items = []
            if (maxIdx > 10):
                # 첫 페이지
                items = items + getListData(type, 0, 0, 5)
                print("---------------- 마지막 페이지 --------------------")

                # 마지막 페이지
                driver.find_element(By.XPATH, '//*[@id="subright"]/form/ul[2]/div/div/ul/a[last()]').click()
                page = int(maxIdx / 10)
                remain = maxIdx % 10
                if (remain >= 5 or remain == 0):
                    items = items + getListData(type, page, remain - 5, remain)
                else:
                    lastItems = getListData(type, page, 0, remain)
                    driver.find_element(By.XPATH, '//*[@id="subright"]/form/ul[2]/div/div/ul/a[2]').click()
                    items = items + getListData(type, page - 1, 5 + remain, 10)
                    items = items + lastItems
            elif (maxIdx > 0):
                items = items + getListData(type, 0, 0, maxIdx)
            else:
                print("검색 결과 없음")

            writeCsv(type, fileName, items)