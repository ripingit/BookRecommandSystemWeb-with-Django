from selenium import webdriver

result = {}

driver = webdriver.Chrome(executable_path='E:\\chromeDriver\\chromedriver_win32 (3)\\chromedriver.exe')

driver.get(url='http://opac.szpt.edu.cn:8991/clc/toc.htm')

for i in driver.find_elements_by_xpath('//div[@class="item"]'):
    print(i.text)