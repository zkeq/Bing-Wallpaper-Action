# coding:utf-8
from http.server import BaseHTTPRequestHandler
import redis
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_bing():
    _params_data = r.srandmember("bing_images", -1)[0].decode('utf-8')
    full_uel = "https://bing.com" + _params_data
    return full_uel


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params_data = get_bing()
        self.send_response(308)  # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', params_data)  # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(params_data))
        # self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600')  # vercel 缓存
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(params_data).encode('utf-8'))  # 这里无所谓
        return None
