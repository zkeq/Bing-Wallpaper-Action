# coding:utf-8
import requests
import json
import time
import os


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def read_update_json(run_type):
    _path = os.path.join(os.path.dirname(__file__), 'data', f'{run_type}_update.json')
    with open(_path, "r", encoding="utf-8") as _f_:
        _data = json.load(_f_)
    return _data


def main(run_type):
    data = requests.get(f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt={run_type}").json()
    print("[{}] 开始读取 API".format(get_now_time()))
    data_list = data["images"]
    write_list = []
    # 写入 data/daily_log/{date}.json
    path = os.path.join(os.path.dirname(__file__), 'data', f'{run_type}_daily_log',
                        "{}_{}.json".format(run_type, get_now_time()).replace(" ", "_").replace(":", "-"))
    with open(path, "w", encoding="utf-8") as _f_:
        json.dump(data, _f_, ensure_ascii=False, indent=4)
    print("[{}] 开始读取更新文件".format(get_now_time()))
    for i in data_list:
        before_data = read_update_json(run_type)
        if i["startdate"] not in before_data["images"][0]["startdate"]:
            print("[{}] 新图片: {}".format(get_now_time(), i["title"]))
            write_list.append(i)
        else:
            break
    print("[{}] 开始更新图片".format(get_now_time()))
    print("[{}] 更新图片数量：{}".format(get_now_time(), len(write_list)))
    # 将write_list写入temp.json
    with open(os.path.join(os.path.dirname(__file__), 'data', f'{run_type}_temp.json'), "w", encoding="utf-8") as _f:
        json.dump(write_list, _f, ensure_ascii=False, indent=4)
    # 读取 data/all.json
    with open(f'data/{run_type}_all.json', 'r', encoding="utf-8") as f:
        all_data = json.load(f)
    print("[{}] 开始更新 {}_all.json".format(run_type, get_now_time()))
    print("[{}] 更新前 {}_all.json 数量：{}".format(get_now_time(), run_type, len(all_data["data"])))

    before_all_list = all_data["data"]
    write_list.extend(before_all_list)

    print("[{}] 更新后 {}_all.json 数量：{}".format(get_now_time(), run_type, len(write_list)))

    data_data = {
        "LastUpdate": get_now_time(),
        "Total": len(write_list),
        "Language": run_type,
        "message": "ok",
        "status": True,
        "success": True,
        "info": "https://raw.onmicrosoft.cn/Bing-Wallpaper-Action/main/data/info.json".
        "data": write_list
    }

    # 保存至 data/all.json
    with open(f'data/{run_type}_all.json', 'w', encoding="utf-8") as f:
        json.dump(data_data, f, ensure_ascii=False, indent=4)

    print("[{}] 更新 {}_all.json 成功".format(get_now_time(), run_type))

    # 保存至 data/update.json
    with open(f'data/{run_type}_update.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("[{}] 更新 {}_update.json 成功".format(get_now_time(), run_type))
