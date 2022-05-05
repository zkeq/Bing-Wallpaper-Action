# coding:utf-8
import os
import main
import post_to_redis

work_list = [
    "ar-XA", "bg-BG", "cs-CZ", "da-DK", "de-AT", "de-CH", "de-DE", "el-GR", "en-AU", "en-CA", "en-GB", "en-ID",
    "en-IE", "en-IN", "en-MY", "en-NZ", "en-PH", "en-SG", "en-US", "en-XA", "en-ZA", "es-AR", "es-CL", "es-ES",
    "es-MX", "es-US", "es-XL", "et-EE", "fi-FI", "fr-BE", "fr-CA", "fr-CH", "fr-FR", "he-IL", "hr-HR", "hu-HU",
    "it-IT", "ja-JP", "ko-KR", "lt-LT", "lv-LV", "nb-NO", "nl-BE", "nl-NL", "pl-PL", "pt-BR", "pt-PT", "ro-RO",
    "ru-RU", "sk-SK", "sl-SI", "sv-SE", "th-TH", "tr-TR", "uk-UA", "zh-CN", "zh-HK", "zh-TW"
]

lang_list = [
    "Arabic – Arabia", "Bulgarian – Bulgaria", "Czech – Czech Republic", "Danish – Denmark", "German – Austria",
    "German – Switzerland", "German – Germany", "Greek – Greece", "English – Australia", "English – Canada",
    "English - United Kingdom", "English – Indonesia", "English – Ireland", "English – India", "English – Malaysia",
    "English – New Zealand", "English – Philippines", "English – Singapore", "English – United States",
    "English – Arabia", "English – South Africa", "Spanish – Argentina", "Spanish – Chile",
    "Spanish – Spain", "Spanish – Mexico", "Spanish – United States", "Spanish – Latin America",
    "Estonian – Estonia", "Finnish – Finland", "French – Belgium", "French – Canada", "French – Switzerland",
    "French – France", "Hebrew – Israel", "Croatian – Croatia", "Hungarian – Hungary", "Italian – Italy",
    "Japanese – Japan", "Korean – Korea", "Lithuanian – Lithuania", "Latvian – Latvia", "Norwegian – Norway",
    "Dutch – Belgium", "Dutch – Netherlands", "Polish – Poland", "Portuguese – Brazil", "Portuguese – Portugal",
    "Romanian – Romania", "Russian – Russia", "Slovak – Slovak Republic", "Slovenian – Slovenia", "Swedish – Sweden",
    "Thai – Thailand", "Turkish – Turkey", "Ukrainian – Ukraine", "Chinese – China", "Chinese – Hong Kong SAR",
    "Chinese – Taiwan"
]


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
    with open("data/template_update.json", "r") as f:
        template_update = f.read()
    return template_update


for i in work_list:
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

