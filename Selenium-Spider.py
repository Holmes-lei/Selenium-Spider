import json
import time
import pandas as pd
from selenium.common import exceptions as ex
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "D:/chromedriver.exe" # 指定自己的chromedriver路径
# time.sleep(3)
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# time.sleep(3)
print(driver.title)
# time.sleep(3)

"""
根据CSS选择器和table中的某一个元素定位其在table中的位置
table包括表头，位置坐标都是从1开始算
cssSelector：table的CSS选择器属性
queryContent：需要确定位置的内容
"""

n = 1   # 翻页次数
i = 0

def get_table_content(cssSelector, n):
    table_list = []
    for i in range(n):
        try:
            locator = cssSelector + ">tbody>tr"
            table_tr_list = driver.find_elements(By.CSS_SELECTOR, locator)[1:]  # 去掉表头
            time.sleep(1)
            for tr in table_tr_list:
                row_list = []
                table_td_list = tr.find_elements(By.TAG_NAME, "td")
                for td in table_td_list:
                    row_list.append(td.text)
                table_list.append(row_list)
        except ex.StaleElementReferenceException:
            time.sleep(3)
            locator = cssSelector + ">tbody>tr"
            table_tr_list = driver.find_elements(By.CSS_SELECTOR, locator)[1:]  # 去掉表头
            for tr in table_tr_list:
                row_list = []
                table_td_list = tr.find_elements(By.TAG_NAME, "td")
                for td in table_td_list:
                    row_list.append(td.text)
                table_list.append(row_list)

        try:
            time.sleep(1)
            if(i < n-1):
                driver.find_element_by_link_text("下一页").click()
            time.sleep(1)
        except ex.StaleElementReferenceException:
            time.sleep(3)
            if (i < n - 1):
                driver.find_element_by_link_text("下一页").click()
            time.sleep(3)


        table_df = pd.DataFrame(table_list, columns=['no', 'level', 'words', 'pinyin', 'character'])
        table_df.to_csv("data_index.csv", index=True, encoding='utf-8')
        table_df.to_csv("data_no_index.csv", index=False, encoding='utf-8')
    table_json = table_df.to_json()
    with open('data.json', 'w') as f:
        json.dump(table_json, f)

    print(table_df)



get_table_content("table", n)

# driver.close()
# https://blog.csdn.net/huayuhuan/article/details/76559465