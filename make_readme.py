# coding:utf-8
"""
README 生成器（v2）

- README.md 只展示最近 30 天的图片，底部附「历史归档」按月索引
- archive/YYYY-MM.md 每个月份一份归档 README，默认只重新生成最新月份
- 首次迁移 / 需要重建全部归档时：python make_readme.py --backfill

数据来源：data/{mkt}_all.json（9 个市场：zh-CN, en-US, ja-JP, de-DE, en-CA, en-GB, en-IN, fr-FR, it-IT）
"""
import json
import os
import sys
import time

# 每个市场一行：(文件名标识, 表头展示名)
MARKETS = [
    ("zh-CN", "Chinese – China"),
    ("en-GB", "English – United Kingdom"),
    ("ja-JP", "Japanese – Japan"),
    ("de-DE", "German – Germany"),
    ("en-CA", "English – Canada"),
    ("en-US", "English – United States"),
    ("en-IN", "English – India"),
    ("fr-FR", "French – France"),
    ("it-IT", "Italian – Italy"),
]

TABLE_GROUPS = [MARKETS[0:3], MARKETS[3:6], MARKETS[6:9]]

RECENT_DAYS = 30
ARCHIVE_DIR = "archive"


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def load_market(mkt):
    path = os.path.join("data", "{}_all.json".format(mkt))
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["data"]


def fmt_date(enddate):
    return "{}-{}-{}".format(enddate[0:4], enddate[4:6], enddate[6:8])


def month_key(enddate):
    """20261008 -> 202610"""
    return enddate[0:6]


def month_file(month):
    """202610 -> archive/2026-10.md"""
    return os.path.join(ARCHIVE_DIR, "{}-{}.md".format(month[0:4], month[4:6]))


def month_label(month):
    """202610 -> 2026年10月"""
    return "{}年{}月".format(month[0:4], int(month[4:6]))


def write_day_row(f, day_entries):
    """写表格的一行，day_entries 与 TABLE_GROUPS 当前组对应（3 个市场各一条）。"""
    cells = []
    for day in day_entries:
        url_full = "https://www.bing.com" + day["urlbase"] + "_UHD.jpg"
        thumb = url_full + "&pid=hp&w=384&h=216&rs=1&c=4"
        cells.append("| ![{0}]({1}) {0} [download 4k]({2})".format(fmt_date(day["enddate"]), thumb, url_full))
    f.write("".join(cells) + "|\n")


def write_tables(f, per_market_entries, row_count):
    """按 3 组 × 3 市场写图片表格。per_market_entries: {mkt: [entries]}"""
    for group in TABLE_GROUPS:
        f.write("\n|  {}  |   {}   |   {}   |\n".format(group[0][1], group[1][1], group[2][1]))
        f.write("| :----: | :----: | :----: |\n")
        for i in range(row_count):
            write_day_row(f, [per_market_entries[mkt][i] for mkt, _ in group])
        f.write("\n-------------------\n")


def write_header(f, latest):
    head_img = "https://www.bing.com" + latest["urlbase"] + "_UHD.jpg"
    f.write("# Bing Wallpaper\n")
    f.write("<!--{}-->\n".format(get_now_time()))
    f.write("![{0}]({2}) Today: [{0}]({1})\n".format(latest["title"], head_img, head_img + "&w=1920"))
    f.write("\n> 本页仅展示最近 {} 天的壁纸，历史图片请查看下方「历史归档」。\n".format(RECENT_DAYS))


def write_archive_index(f, months):
    """README 底部：按月归档索引，新月份在前。"""
    f.write("\n## 📦 历史归档\n\n")
    by_year = {}
    for m in months:
        by_year.setdefault(m[0:4], []).append(m)
    for year in sorted(by_year.keys(), reverse=True):
        links = ["[{}]({})".format(month_label(m), month_file(m).replace(os.sep, "/")) for m in sorted(by_year[year], reverse=True)]
        f.write("- {} 年：{}\n".format(year, " · ".join(links)))
    f.write("\n")


def write_month_archive(market_data, month, months_all):
    """生成某个月的归档 README。"""
    per_market = {}
    for mkt, _ in MARKETS:
        per_market[mkt] = [e for e in market_data[mkt] if month_key(e["enddate"]) == month]
    row_count = min(len(v) for v in per_market.values())
    if row_count == 0:
        print("[{}] 月份 {} 无数据，跳过".format(get_now_time(), month))
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    path = month_file(month)
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Bing Wallpaper · {}归档\n".format(month_label(month)))
        f.write("\n> 共 {} 天 · [返回首页](../README.md)\n".format(row_count))
        # 当月相邻月份导航
        idx = months_all.index(month)
        nav = []
        if idx > 0:
            newer = months_all[idx - 1]
            nav.append("[← {}]({})".format(month_label(newer), os.path.basename(month_file(newer))))
        if idx < len(months_all) - 1:
            older = months_all[idx + 1]
            nav.append("[{} →]({})".format(month_label(older), os.path.basename(month_file(older))))
        if nav:
            f.write("\n" + " · ".join(nav) + "\n")
        write_tables(f, per_market, row_count)
    print("[{}] 已生成 {}".format(get_now_time(), path))


def main():
    backfill = "--backfill" in sys.argv

    market_data = {}
    for mkt, _ in MARKETS:
        market_data[mkt] = load_market(mkt)
    total_days = min(len(v) for v in market_data.values())
    print("[{}] all day: {}".format(get_now_time(), total_days))

    # 所有出现过的月份（新 → 旧）
    months = sorted({month_key(e["enddate"]) for v in market_data.values() for e in v}, reverse=True)
    print("[{}] 归档月份数: {}（{} ~ {}）".format(get_now_time(), len(months), months[-1], months[0]))

    # ---------- README.md：最近 30 天 ----------
    recent = {mkt: market_data[mkt][:RECENT_DAYS] for mkt, _ in MARKETS}
    row_count = min(len(v) for v in recent.values())
    latest = market_data["zh-CN"][0]

    with open("README.md", "w", encoding="utf-8") as f:
        write_header(f, latest)
        write_tables(f, recent, row_count)
        write_archive_index(f, months)
    print("[{}] README.md 已生成（最近 {} 天）".format(get_now_time(), row_count))

    # ---------- 按月归档 ----------
    if backfill:
        targets = months
        print("[{}] backfill 模式：重建全部 {} 个月份归档".format(get_now_time(), len(targets)))
    else:
        targets = months[:1]
        print("[{}] 增量模式：仅更新最新月份 {}".format(get_now_time(), month_label(targets[0])))
    for m in targets:
        write_month_archive(market_data, m, months)


if __name__ == "__main__":
    main()
