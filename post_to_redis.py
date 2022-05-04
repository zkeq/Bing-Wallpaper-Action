# coding:utf-8

import redis
import json
import time
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 读取 data/temo.json
with open('data/temp.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

print("[{}] 开始更新 redis".format(get_now_time()))

for i in data:
    print("[{}] 更新图片：{}".format(get_now_time(), i["title"]))
    r.sadd("bing_images", i["url"])

print("[{}] 更新完成".format(get_now_time()))
