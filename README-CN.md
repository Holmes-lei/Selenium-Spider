# Selenium-Spider

Bypassing the login screen to crawl table data using Selenium.

## 爬取目标

> [汉语考试服务网](http://www.chinesetest.cn/userlogin.do)
> 
> <img width="1090" alt="截屏2022-05-07 11 16 46" src="https://user-images.githubusercontent.com/47048401/167235903-c1ab39dd-17d3-478d-a06b-639c6aca2662.png">


## 爬取方法

1. 绕过登录界面。手动登录网站后，由Selenium接管当前页面。

> <img width="742" alt="截屏2022-05-07 11 16 13" src="https://user-images.githubusercontent.com/47048401/167235911-acc3cd56-3e2f-415c-9e04-ca882a2bcd98.png">

2. 自动点击翻页。设置time.sleep()等待页面刷新，否则会获取元素失败。

## 使用方法

1. 第25行，n的值为table需要翻页的次数

```python
n = 1   # 翻页次数
```



2. 第55和第60行，根据页面上的"下一页"文字来选中并点击。因此如果网页上显示的向下翻页的名字叫"下一页"则不用修改，如果是别的类似"next"，则要把"下一页"替换为"next"

```python
driver.find_element_by_link_text("下一页").click()
```

3. 第64行，columns=['']中填写表格的列项

```python
table_df = pd.DataFrame(table_list, columns=['no', 'level', 'words', 'pinyin', 'character'])
```

4. 第65，66，68行，请指定自己的文件名

```python
table_df.to_csv("data_index.csv", index=True, encoding='utf-8')
table_df.to_csv("data_no_index.csv", index=False, encoding='utf-8')
with open('data.json', 'w') as f:
```

