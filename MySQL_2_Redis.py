# coding: utf-8
import json

import pymysql
import redis
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


# 连接本地数据库
db = pymysql.connect(host='localhost', user='root', password='Zkeq', port=3306, db='bing')
cursor = db.cursor()
# 执行sql语句
sql = "SELECT `image` FROM `bing`"
cursor.execute(sql)
# 获取所有记录列表
results = list(cursor.fetchall())
for i in results:
    itme = i[0]
    print(itme)
    # 推送到 redis
    r.sadd("bing_images", itme)

# 关闭数据库连接
db.close()
