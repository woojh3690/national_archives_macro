from selenium.webdriver.common.by import By

end = '  |  '

# 기본 파싱
def parse_default(driver, page, startIdx = 0, endIdx = 5):
    listMngNoXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/dl/dd[3]'
    listTitleXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[1]/label'
    listBtnXpath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[2]/a[1]'
    listSubTitleXPath = '//*[@id="detial_{}"]/table[1]/tbody/tr[1]/td/a'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        item = []
        searchIdx = page * 10 + idx
        print(searchIdx, end=end)

        texts = driver.find_element(By.XPATH, listMngNoXPath.format(idx)).text
        item.append(texts)
        item.append(searchIdx)  # 검색순위
        item.append(' ')  # 매칭된 질의어 키워드
        print(texts, end=end)

        texts = driver.find_element(By.XPATH, listTitleXPath.format(idx)).text
        item.append(texts)
        print(texts, end=end)

        driver.find_element(By.XPATH, listBtnXpath.format(idx)).click()
        texts = driver.find_element(By.XPATH, listSubTitleXPath.format(idx - 1)).text
        item.append(texts)
        print(texts)

        items.append(item)
    return items

# 관보 파싱
def parse_gazette(driver, page, startIdx = 0, endIdx = 5):
    listMngNoXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/dl/dd[3]'
    listTitleXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[1]/label'
    listBtnXpath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[2]/a[1]'
    listSubTitleXPath = '//*[@id="detial_{}"]/table[1]/tbody/tr[1]/td/a'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        searchIdx = page * 10 + idx
        
        # 타이틀
        title = driver.find_element(By.XPATH, listTitleXPath.format(idx)).text
        
        # 하위 타이틀
        subTitle = driver.find_element(By.XPATH, listMngNoXPath.format(idx)).text
        
        # 탭 전환
        driver.find_element(By.XPATH, listBtnXpath.format(idx)).click()
        driver.switch_to.window(driver.window_handles[-1])
        mngNo = driver.find_element(By.XPATH, '//*[@id="contents"]/div/div[1]/table/tbody/tr[5]/td[2]').text

        # 탭 닫기
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

        print(searchIdx, end=end)
        print(mngNo, end=end)
        print(title, end=end)
        print(subTitle)
        
        items.append([mngNo, searchIdx, ' ', title, subTitle])
    return items

# 국무 회의록 파싱
def parse_proceedings(driver, page, startIdx = 0, endIdx = 5):
    listMngNoXPath = '//*[@id="detial_{}"]/table/tbody/tr[4]/td[2]'
    listTitleXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[1]/label'
    listBtnXpath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[2]/a[1]'
    listSubTitleXPath = '//*[@id="detial_{}"]/table/tbody/tr[1]/td'
    listSubTitle2XPath = '//*[@id="detial_{}"]/table/tbody/tr[2]/td'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        searchIdx = page * 10 + idx

        title = driver.find_element(By.XPATH, listTitleXPath.format(idx)).text
    
        driver.find_element(By.XPATH, listBtnXpath.format(idx)).click()
        mngNo = driver.find_element(By.XPATH, listMngNoXPath.format(idx - 1)).text
        gunTitle = driver.find_element(By.XPATH, listSubTitleXPath.format(idx - 1)).text
        ironTitle = driver.find_element(By.XPATH, listSubTitle2XPath.format(idx - 1)).text

        print(searchIdx, end=end)
        print(mngNo, end=end)
        print(title, end=end)
        print(gunTitle, end=end)
        print(ironTitle)

        items.append([mngNo, searchIdx, ' ', title, gunTitle, ironTitle])
    return items

# 국무 회의록 파싱
def parse_proceedings(driver, page, startIdx = 0, endIdx = 5):
    listMngNoXPath = '//*[@id="detial_{}"]/table/tbody/tr[4]/td[2]'
    listTitleXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[1]/label'
    listBtnXpath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[2]/a[1]'
    listSubTitleXPath = '//*[@id="detial_{}"]/table/tbody/tr[1]/td'
    listSubTitle2XPath = '//*[@id="detial_{}"]/table/tbody/tr[2]/td'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        searchIdx = page * 10 + idx
        
        title = driver.find_element(By.XPATH, listTitleXPath.format(idx)).text
    
        driver.find_element(By.XPATH, listBtnXpath.format(idx)).click()
        mngNo = driver.find_element(By.XPATH, listMngNoXPath.format(idx - 1)).text
        gunTitle = driver.find_element(By.XPATH, listSubTitleXPath.format(idx - 1)).text
        ironTitle = driver.find_element(By.XPATH, listSubTitle2XPath.format(idx - 1)).text

        print(searchIdx, end=end)
        print(mngNo, end=end)
        print(title, end=end)
        print(gunTitle, end=end)
        print(ironTitle)

        items.append([mngNo, searchIdx, ' ', title, gunTitle, ironTitle])
    return items

# 일제강점기 기록물
def parse_record(driver, page, startIdx = 0, endIdx = 5):
    listMngNoXPath = '//*[@id="contents"]/div[3]/dl/dd[4]'
    listTitleXPath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[1]/label'
    listBtnXpath = '//*[@id="subright"]/form/ul[2]/li[{}]/div[2]/a[1]'
    listSubTitleXPath = '//*[@id="view01"]/div[1]/table/tbody/tr[1]/td'

    items = []
    for idx in range(startIdx + 1, endIdx + 1):
        searchIdx = page * 10 + idx
        
        # 타이틀
        title = driver.find_element(By.XPATH, listTitleXPath.format(idx)).text
        
        # 탭 전환
        driver.find_element(By.XPATH, listBtnXpath.format(idx)).click()
        driver.switch_to.window(driver.window_handles[-1])

        # 관리번호
        mngNo = driver.find_element(By.XPATH, listMngNoXPath).text[2:]

        # 하위 타이틀
        subTitle = driver.find_element(By.XPATH, listSubTitleXPath).text   

        # 탭 닫기
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

        print(searchIdx, end=end)
        print(mngNo, end=end)
        print(title, end=end)
        print(subTitle)
        
        items.append([mngNo, searchIdx, ' ', title, subTitle])
    return items