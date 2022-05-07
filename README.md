# Selenium-Spider
Bypassing the login screen to crawl table data using Selenium.

> [中文README](https://github.com/Holmes-lei/Selenium-Spider/blob/main/README-CN.md)

## Crawl Target

> [汉语考试服务网](http://www.chinesetest.cn/userlogin.do)
>
> <img width="1090" alt="截屏2022-05-07 11 16 46" src="https://user-images.githubusercontent.com/47048401/167235903-c1ab39dd-17d3-478d-a06b-639c6aca2662.png">


## Crawl Method

1. Bypass the login screen. After manually logging into the site, Selenium takes over the current page.

> <img width="742" alt="截屏2022-05-07 11 16 13" src="https://user-images.githubusercontent.com/47048401/167235911-acc3cd56-3e2f-415c-9e04-ca882a2bcd98.png">

2. Automatically click to turn the page. Set time.sleep() to wait for the page to refresh, otherwise it will fail to fetch the element.

## How To Use

1. Row 25, the value of n is the number of times the table needs to be page-flipped.

```python
n = 1   # 翻页次数
```



2. For lines 55 and 60, select and click on the "下一页" text on the page. So if the name of the page displayed on the page is "下一页", you don't need to change it, but if it is something like "next", you should replace "下一页" with "next".

```python
driver.find_element_by_link_text("下一页").click()
```

3. Line 64, columns=[''] is filled with the column entries of the table.

```python
table_df = pd.DataFrame(table_list, columns=['no', 'level', 'words', 'pinyin', 'character'])
```

4. Lines 65, 66, 68, please specify your own file name.

```python
table_df.to_csv("data_index.csv", index=True, encoding='utf-8')
table_df.to_csv("data_no_index.csv", index=False, encoding='utf-8')
with open('data.json', 'w') as f:
```





