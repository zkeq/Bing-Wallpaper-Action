# coding:utf-8
import json
import time


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 读取 data/zh-CN_all.json 文件，生成 README.md 文件
with open('data/zh-CN_all.json', 'r', encoding='utf-8') as f:
    zh_data = json.load(f)

with open('data/en-US_all.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open('data/ja-JP_all.json', 'r', encoding='utf-8') as f:
    ja_data = json.load(f)

all_day = len(zh_data['data'])
print("[{}] all day: {}".format(get_now_time(), all_day))

head_img = "https://www.bing.com" + zh_data['data'][0]['urlbase'] + "_UHD.jpg" + "&w=1000"
head_des = zh_data['data'][0]['copyright']
head_title = zh_data['data'][0]['title']

f = open('README.md', 'w', encoding='utf-8')
f.write("# Bing Wallpaper\n")
f.write(f"<!--{get_now_time()}-->\n")
f.write("![{0}]({1}) Today: [{0}]({1})\n".format(head_title, head_img))
f.write("""
|  zh-CN   |   en-US   |   ja-JP   |
| :----: | :----: | :----: |
""")
for i in range(all_day):
    print("[{}] day: {}".format(get_now_time(), i + 1))
    zh_day = zh_data['data'][i]
    en_day = en_data['data'][i]
    ja_day = ja_data['data'][i]
    zh_date = zh_day['startdate']
    zh_date_format = "{}-{}-{}".format(zh_date[0:4], zh_date[4:6], zh_date[6:8])
    en_date = en_day['startdate']
    en_date_format = "{}-{}-{}".format(en_date[0:4], en_date[4:6], en_date[6:8])
    ja_date = ja_day['startdate']
    ja_date_format = "{}-{}-{}".format(ja_date[0:4], ja_date[4:6], ja_date[6:8])
    zh_url_full = "https://www.bing.com" + zh_day['urlbase'] + "_UHD.jpg" + "&pid=hp&w=384&h=216&rs=1&c=4"
    en_url_full = "https://www.bing.com" + en_day['urlbase'] + "_UHD.jpg" + "&pid=hp&w=384&h=216&rs=1&c=4"
    ja_url_full = "https://www.bing.com" + ja_day['urlbase'] + "_UHD.jpg" + "&pid=hp&w=384&h=216&rs=1&c=4"
    f.write("| ![{0}]({1}) {0} [download 4k]({1})| ![{2}]({3}) {2} [download 4k]({3})| ![{4}]({5}) {4} [download 4k]({5})|\n".format(zh_date_format, zh_url_full, en_date_format, en_url_full, ja_date_format, ja_url_full))
f.close()