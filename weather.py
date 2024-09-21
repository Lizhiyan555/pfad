
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url1 = 'https://lishi.tianqi.com/shenzhen/202402.html'
url2 = 'https://lishi.tianqi.com/shenzhen/202403.html'


def get_data(url):
    headers = {"User-Agent":
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
               }
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')

    bs = BeautifulSoup(html, 'html.parser')
    lis = bs.body.find('div', {'class': 'tian_three'}
                       ).find('ul').find_all('li')
    w = []
    for li in lis:
        temp = []
        divs = li.find_all('div')
        for d in divs:
            temps = d.string.replace("℃", "").replace(" ", "")
            temp.append(temps)
        w.append(temp)
    return w


def data_proc(w):
    df = pd.DataFrame(w, columns=['日期星期', '最高气温', '最低气温', '天气', '风向'])
    df = df.drop_duplicates()
    df = df.assign(日期=df.日期星期.str.slice(0, 10)).assign(
        星期=df.日期星期.str.slice(10, 13)).drop('日期星期', axis=1)
    df.最高气温 = df.最高气温.astype(int)
    df.最低气温 = df.最低气温.astype(int)
    df = df.assign(风力=df.风向.map(
        lambda x: ''.join(list(filter(str.isdigit, x)))))
    df['平均气温'] = (df.最高气温 + df.最低气温) / 2
    df.风力 = df.风力.astype(int)
    df.平均气温 = df.平均气温.astype(float)
    return df


df1 = data_proc(get_data(url1))
df2 = data_proc(get_data(url2))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12, 6))
x = range(0, len(df1))
plt.plot(x, df1['最高气温'], label='最高气温')
plt.plot(x, df1['最低气温'], label='最低气温')
plt.xticks(x, df1['日期'], rotation=30)
plt.legend()

plt.show()

c1 = len(df1.query("(平均气温>=18) and (平均气温<=25) and (风力<5)"))
c2 = len(df2.query("(平均气温>=18) and (平均气温<=25) and (风力<5)"))
plt.bar(['2月', '3月'], [c1, c2], width=0.5)
plt.xlabel('月份')
plt.ylabel('天数')
plt.show()


res1 = {}
for k, v in dict([x for x in df1.groupby('天气')]).items():
    res1[k] = len(v)
res2 = {}
for k, v in dict([x for x in df2.groupby('天气')]).items():
    res2[k] = len(v)
for k in res2:
    if res1.get(k) is None:
        res1[k] = 0
for k in res1:
    if res2.get(k) is None:
        res2[k] = 0
x = range(0, len(res1))
plt.figure(figsize=(12, 6))
plt.bar([i - 0.2 for i in x], res1.values(), width=0.4, label='2月')
plt.bar([i + 0.2 for i in x], res2.values(), width=0.4, label='3月')
plt.xticks(x, res1.keys())
plt.xlabel('天气')
plt.ylabel('天数')
plt.legend()
plt.show()

