# coding:utf-8
import os
import time

import main
import post_to_redis
import sys


# work_list = [
#     "de-DE", "en-CA", "en-GB", "en-IN", "en-US", "fr-FR", "it-IT", "ja-JP", "zh-CN"
# ]


# 判断文件是否存在
def file_exists(file_path):
    return os.path.exists(file_path)


# 判断文件夹是否存在
def dir_exists(dir_path):
    return os.path.isdir(dir_path)


def get_all_template():
    # 读取 data/template_all.json 文件
    with open("data/template_all.json", "r") as f:
        template_all = f.read()
    return template_all


def get_update_template():
    # 读取 data/template_update.json 文件
    with open("data/template_update.json", "r") as _f:
        template_update = _f.read()
    return template_update


i = sys.argv[1]

if not file_exists(f"data/{i}_all.json"):
    # 创建文件
    with open(f"data/{i}_all.json", "w", encoding="utf-8") as f:
        f.write(get_all_template())
if not file_exists(f"data/{i}_update.json"):
    # 创建文件
    with open(f"data/{i}_update.json", "w", encoding="utf-8") as f:
        f.write(get_update_template())
if not dir_exists(f"data/{i}_daily_log"):
    # 创建文件夹
    os.mkdir(f"data/{i}_daily_log")
main.main(i)
post_to_redis.main(i)
time.sleep(3)

