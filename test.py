# import requests
# import redis
#
# r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# r_remote = redis.Redis(
#     host='apn1-destined-giraffe-32369.upstash.io',
#     port=32369,
#     password='', ssl=True)
#
# # data = requests.get("https://api.github.com/users/valetzx/starred").json()
# # for i in data:
# #     print('项目名', i["full_name"])
# #     print("描述", i["description"])
# #     print("链接", i["html_url"])
#
# # 查询集合中的所有元素
# # print(r.smembers("bing_images"))
#
# print("local database counter：", r.scard("bing_images"))
# # 随机获取一个元素
# print("https://bing.com" + r.srandmember("bing_images").decode('utf-8'))
# print("https://bing.com" + r.srandmember("bing_images").decode('utf-8'))
# print("https://bing.com" + r.srandmember("bing_images").decode('utf-8'))
# print("https://bing.com" + r.srandmember("bing_images").decode('utf-8'))
# print("https://bing.com" + r.srandmember("bing_images").decode('utf-8'))
#
# print("remote database counter：", r_remote.scard("bing_images"))
# print("https://bing.com" + r_remote.srandmember("bing_images", -1)[0].decode('utf-8'))
# print("https://bing.com" + r_remote.srandmember("bing_images", -1)[0].decode('utf-8'))
# print("https://bing.com" + r_remote.srandmember("bing_images", -1)[0].decode('utf-8'))
# print("https://bing.com" + r_remote.srandmember("bing_images", -1)[0].decode('utf-8'))
# print("https://bing.com" + r_remote.srandmember("bing_images", -1)[0].decode('utf-8'))
import sys

a = sys.argv
print(a)