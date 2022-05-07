# coding:utf-8
import json
import time


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


#   "zh-CN", "en-US", "ja-JP", "de-DE", "en-CA", "en-GB", "en-IN",  "fr-FR", "it-IT"
# 读取 data/zh-CN_all.json 文件，生成 README.md 文件
with open('data/zh-CN_all.json', 'r', encoding='utf-8') as f:
    zh_data = json.load(f)

with open('data/en-US_all.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open('data/ja-JP_all.json', 'r', encoding='utf-8') as f:
    ja_data = json.load(f)

with open('data/de-DE_all.json', 'r', encoding='utf-8') as f:
    de_data = json.load(f)

with open('data/en-CA_all.json', 'r', encoding='utf-8') as f:
    en_ca_data = json.load(f)

with open('data/en-GB_all.json', 'r', encoding='utf-8') as f:
    en_gb_data = json.load(f)

with open('data/en-IN_all.json', 'r', encoding='utf-8') as f:
    en_in_data = json.load(f)

with open('data/fr-FR_all.json', 'r', encoding='utf-8') as f:
    fr_data = json.load(f)

with open('data/it-IT_all.json', 'r', encoding='utf-8') as f:
    it_data = json.load(f)


all_day = min(
    len(zh_data['data']),
    len(en_data['data']),
    len(ja_data['data']),
    len(de_data['data']),
    len(en_ca_data['data']),
    len(en_gb_data['data']),
    len(en_in_data['data']),
    len(fr_data['data']),
    len(it_data['data'])
)
print("[{}] all day: {}".format(get_now_time(), all_day))

head_img = "https://www.bing.com" + zh_data['data'][0]['urlbase'] + "_UHD.jpg"
head_des = zh_data['data'][0]['copyright']
head_title = zh_data['data'][0]['title']

f = open('README.md', 'w', encoding='utf-8')
f.write("# Bing Wallpaper\n")
f.write(f"<!--{get_now_time()}-->\n")
f.write("![{0}]({2}) Today: [{0}]({1})\n".format(head_title, head_img, head_img + "&w=1920"))
f.write("""
|  Chinese – China   |   English – United Kingdom   |   Japanese – Japan   |
| :----: | :----: | :----: |
""")
for i in range(all_day):
    print("[{}] day: {}".format(get_now_time(), i + 1))
    zh_day = zh_data['data'][i]
    en_day = en_data['data'][i]
    ja_day = ja_data['data'][i]
    zh_date = zh_day['enddate']
    zh_date_format = "{}-{}-{}".format(zh_date[0:4], zh_date[4:6], zh_date[6:8])
    en_date = en_day['enddate']
    en_date_format = "{}-{}-{}".format(en_date[0:4], en_date[4:6], en_date[6:8])
    ja_date = ja_day['enddate']
    ja_date_format = "{}-{}-{}".format(ja_date[0:4], ja_date[4:6], ja_date[6:8])
    zh_url_full = "https://www.bing.com" + zh_day['urlbase'] + "_UHD.jpg"
    zh_readme_url = zh_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    en_url_full = "https://www.bing.com" + en_day['urlbase'] + "_UHD.jpg"
    en_readme_url = en_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    ja_url_full = "https://www.bing.com" + ja_day['urlbase'] + "_UHD.jpg"
    ja_readme_url = ja_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    f.write("| ![{0}]({1}) {0} [download 4k]({6})| ![{2}]({3}) {2} [download 4k]({7})| ![{4}]({5}) {4} [download 4k]({8})|\n".format(zh_date_format, zh_readme_url, en_date_format, en_readme_url, ja_date_format, ja_readme_url, zh_url_full, en_url_full, ja_url_full))

f.write("-------------------\n")

f.write("""
|  German – Germany   |   English – Canada   |   English – United States   |
| :----: | :----: | :----: |
""")
for i in range(all_day):
    print("[{}] day: {}".format(get_now_time(), i + 1))
    de_day = de_data['data'][i]
    en_ca_day = en_ca_data['data'][i]
    en_gb_day = en_gb_data['data'][i]
    de_date = de_day['enddate']
    de_date_format = "{}-{}-{}".format(de_date[0:4], de_date[4:6], de_date[6:8])
    en_ca_date = en_ca_day['enddate']
    en_ca_date_format = "{}-{}-{}".format(en_ca_date[0:4], en_ca_date[4:6], en_ca_date[6:8])
    en_gb_date = en_gb_day['enddate']
    en_gb_date_format = "{}-{}-{}".format(en_gb_date[0:4], en_gb_date[4:6], en_gb_date[6:8])
    de_url_full = "https://www.bing.com" + de_day['urlbase'] + "_UHD.jpg"
    de_readme_url = de_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    en_ca_url_full = "https://www.bing.com" + en_ca_day['urlbase'] + "_UHD.jpg"
    en_ca_readme_url = en_ca_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    en_gb_url_full = "https://www.bing.com" + en_gb_day['urlbase'] + "_UHD.jpg"
    en_gb_readme_url = en_gb_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    f.write("| ![{0}]({1}) {0} [download 4k]({6})| ![{2}]({3}) {2} [download 4k]({7})| ![{4}]({5}) {4} [download 4k]({8})|\n".format(de_date_format, de_readme_url, en_ca_date_format, en_ca_readme_url, en_gb_date_format, en_gb_readme_url, de_url_full, en_ca_url_full, en_gb_url_full))

f.write("-------------------\n")

f.write("""
|  English – India  |   French – France   |   Italian – Italy   |
| :----: | :----: | :----: |
""")

for i in range(all_day):
    print("[{}] day: {}".format(get_now_time(), i + 1))
    en_in_day = en_in_data['data'][i]
    fr_fr_day = fr_data['data'][i]
    it_it_day = it_data['data'][i]
    en_in_date = en_in_day['enddate']
    en_in_date_format = "{}-{}-{}".format(en_in_date[0:4], en_in_date[4:6], en_in_date[6:8])
    fr_fr_date = fr_fr_day['enddate']
    fr_fr_date_format = "{}-{}-{}".format(fr_fr_date[0:4], fr_fr_date[4:6], fr_fr_date[6:8])
    it_it_date = it_it_day['enddate']
    it_it_date_format = "{}-{}-{}".format(it_it_date[0:4], it_it_date[4:6], it_it_date[6:8])
    en_in_url_full = "https://www.bing.com" + en_in_day['urlbase'] + "_UHD.jpg"
    en_in_readme_url = en_in_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    fr_fr_url_full = "https://www.bing.com" + fr_fr_day['urlbase'] + "_UHD.jpg"
    fr_fr_readme_url = fr_fr_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    it_it_url_full = "https://www.bing.com" + it_it_day['urlbase'] + "_UHD.jpg"
    it_it_readme_url = it_it_url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
    f.write("| ![{0}]({1}) {0} [download 4k]({6})| ![{2}]({3}) {2} [download 4k]({7})| ![{4}]({5}) {4} [download 4k]({8})|\n".format(en_in_date_format, en_in_readme_url, fr_fr_date_format, fr_fr_readme_url, it_it_date_format, it_it_readme_url, en_in_url_full, fr_fr_url_full, it_it_url_full))