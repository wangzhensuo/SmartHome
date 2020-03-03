user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
def biying(words):
    # 导入requests模块
    import requests
    # 翻译的内容
    # words = input('请输入你要翻译的内容:')
    # 翻译的内容,及格式打包成一个字典
    data = {
        'text': words,
        'from': 'ja',
        'to': 'zh-CHS'
    }
    # 必应翻译翻译时的网址
    url = 'https://cn.bing.com/ttranslate?&category=&IG=0DB37A4E4FCB479C990C0EEE9419B058'
    # 将网址和请求包传入requests模块,以post请求的方式发送出去
    result = requests.post(url, data)
    # 以文本的形式打印结果
    # print(result.text)
    # 以json的形式打印结果,并利用索引去除不需要的内容
    # print(result.json()['translationResponse'])
    ret = result.json()['translationResponse']
    print(ret)
    return ret

# biying("人民網が主催する世界湾区合作発展フォーラム")
import requests
import json
import base64
import os
import logging
import speech_recognition as sr


def get_token():
    logging.info('开始获取token...')
    #获取token
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "up7sdaBHdk09sbMk1l6ijszx"
    client_secret = "XmoFEcE4i8ErqBbnuSlgWb2B81AKXard"

    #拼url
    url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token


def audio_baidu(filename):
    logging.info('开始识别语音文件...')
    with open(filename, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(filename)
    token = get_token()
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": "1536",
        "speech": speech,
        "cuid": "TEDxPY",
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)

    if result["err_msg"] == "success.":
        # print(result['result'])
        return result['result']
    else:
        print("没有获取到内容")
        # return -1
def my_translate(in_str):
    import requests
    import json
    url = "https://aidemo.youdao.com/trans"
    # ret=u"文本太长啦"
    data = {
        "q": in_str,
        "from": "ja",
        "to": "zh-CHS"}

    headers = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
        "Referer": "https://ai.youdao.com/product-fanyi.s"
    }

    response = requests.post(url, data=data, headers=headers)
    html_str = response.content.decode()  # json字符串
    dict_ret = json.loads(html_str)
    print(dict_ret)
    ret = dict_ret["translation"]
    # print("翻译结果是：", ret)
    # print("\n")
    return ret
def voice_ch(in_str,out_name):
    import requests,time,random
    import json
    url = "https://fanyi.baidu.com/gettts?lan=zh&text="+in_str+"&spd=5&source=web"

    data = {
        "lan": "ch",
        "text": in_str,
        "spd": 5,
        "source":"web"
    }

    headers = {
        "User-Agent": random.choice(user_agent_list),
        "Referer": "https://fanyi.baidu.com/"
    }

    response = requests.get(url, data=data, headers=headers)
    # time.sleep(1)
    print(response.content)
    # ch_mp3 = '{:0>3d}{}.mp3'.format(out_name,in_str)
    # print(ch_mp3)
    import random
    r1=random.randint(1,11111)
    with open(r'.\\mp3\\'+str(r1)+'.mp3','wb') as f:
        f.write(response.content)
    play_music(r'.\mp3\\'+str(r1)+'.mp3')
    os.remove(r'.\mp3\\'+str(r1)+'.mp3')
def voice_jp(in_str,out_name):
    import requests,time,random
    import json
    url = "https://fanyi.baidu.com/gettts?lan=jp&text="+in_str+"&spd=3&source=web"

    data = {
        "lan": "ja",
        "text": in_str,
        "spd": 3,
        "source":"web"
    }

    headers = {
        "User-Agent": random.choice(user_agent_list),
        "Referer": "https://fanyi.baidu.com/"
    }

    response = requests.get(url, data=data, headers=headers)
    # time.sleep(1)
    print(response.content)
    # ch_mp3 = '{:0>3d}{}.mp3'.format(out_name,in_str)
    # print(ch_mp3)
    import random
    r1=random.randint(22222,33333)
    with open(r'.\\mp3\\'+str(r1)+'.mp3','wb') as f:
        f.write(response.content)
    play_music(r'.\mp3\\'+str(r1)+'.mp3')
    os.remove(r'.\mp3\\'+str(r1)+'.mp3')
def play_music(filename):
    import mp3play
    from playsound import playsound
    # print('filename'+filename)
    playsound(filename)
def biying(words):
    # 导入requests模块
    import requests
    # 翻译的内容
    # words = input('请输入你要翻译的内容:')
    # 翻译的内容,及格式打包成一个字典
    data = {
        'text': words,
        'from': 'zh-CHS',
        'to': 'en'
    }
    # 必应翻译翻译时的网址
    url = 'https://cn.bing.com/ttranslate?&category=&IG=0DB37A4E4FCB479C990C0EEE9419B058'
    # 将网址和请求包传入requests模块,以post请求的方式发送出去
    result = requests.post(url, data)
    # 以文本的形式打印结果
    # print(result.text)
    # 以json的形式打印结果,并利用索引去除不需要的内容
    # print(result.json()['translationResponse'])
    ret = result.json()['translationResponse']
    print("翻译为英文： "+ret)
    return ret

def biying_jp(words):
    # 导入requests模块
    import requests
    # 翻译的内容
    # words = input('请输入你要翻译的内容:')
    # 翻译的内容,及格式打包成一个字典
    # print('日文'+words)
    data = {
        'text': words,
        'from': 'zh-CHS',
        'to': 'ja'
    }
    # 必应翻译翻译时的网址
    url = 'https://cn.bing.com/ttranslate?&category=&IG=0DB37A4E4FCB479C990C0EEE9419B058'
    # 将网址和请求包传入requests模块,以post请求的方式发送出去
    result = requests.post(url, data)
    # 以文本的形式打印结果
    # print(result.text)
    # 以json的形式打印结果,并利用索引去除不需要的内容
    # print(result.json()['translationResponse'])
    ret = result.json()['translationResponse']
    print("翻译为日文:"+ret)
    return ret

if __name__ == "__main__":
    # from playsound import playsound
    # # playsound('私に試してみてください')
    # playsound(u'中文')
    # voice_ch("hello",1)
    logging.basicConfig(level=logging.INFO)

    wav_num = 0
    while True:
        r = sr.Recognizer()
        #启用麦克风
        mic = sr.Microphone()
        logging.info('录音中...')
        with mic as source:
            #降噪
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        with open(f"00{wav_num}.wav", "wb") as f:
            #将麦克风录到的声音保存为wav文件
            f.write(audio.get_wav_data(convert_rate=16000))
        logging.info('录音结束，识别中...')
        target = audio_baidu(f"00{wav_num}.wav")
        if target == -1:
            break
        # print(target)
        if target==None:
            wav_num += 1
            continue
        print('='*30)
        print('语音识别结果：'+"".join(target))

        voice_jp(biying_jp(str("".join(target))), 1)
        voice_ch(biying(str("".join(target))), 1)
        wav_num += 1
#!/usr/bin/env python
# # coding=utf-8
# from gevent import monkey
# from gevent.pool import Pool
# import gevent
# import time
# import os
# import csv
# import logging
# from pprint import pprint
# from collections import Counter
#
#
# import matplotlib.pyplot as plt
# import jieba
# import pymysql
#
# from queue import Queue
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import sys
#
# # Make the standard library cooperative.
# monkey.patch_all()
# import requests
#
# def get_logger():
#     """
#     创建日志实例
#     """
#     formatter = logging.Formatter("%(asctime)s - %(message)s")
#     logger = logging.getLogger("monitor")
#     logger.setLevel(LOG_LEVEL)
#
#     ch = logging.StreamHandler()
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     return logger
#
#
# HEADERS = {
#     "X-Requested-With": "XMLHttpRequest",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
#     "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
# }
#
# START_URL = (
#     "http://search.51job.com/list/010000%252C020000%252C030200%252C040000"
#     ",000000,0000,00,9,99,Python,2,{}.html? lang=c&stype=1&postchannel=00"
#     "00&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lon"
#     "lat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&"
#     "address=&line=&specialarea=00&from=&welfare="
# )
#
# LOG_LEVEL = logging.INFO    # 日志等级
# POOL_MAXSIZE = 8  # 线程池最大容量
#
# logger = get_logger()
#
#
# class JobSpider:
#     """
#     51 job 网站爬虫类
#     """
#
#     def __init__(self):
#         self.count = 1  # 记录当前爬第几条数据
#         self.company = []
#         self.desc_url_queue = Queue()  # 线程池队列
#         self.pool = Pool(POOL_MAXSIZE)  # 线程池管理线程,最大协程数
#
#     def job_spider(self):
#         """
#         爬虫入口
#         """
#         urls = [START_URL.format(p) for p in range(1, 16)]
#         for url in urls:
#             logger.info("爬取第 {} 页".format(urls.index(url) + 1))
#             html = requests.get(url, headers=HEADERS).content.decode("gbk")
#             bs = BeautifulSoup(html, "lxml").find("div", class_="dw_table").find_all(
#                 "div", class_="el"
#             )
#             for b in bs:
#                 try:
#                     href, post = b.find("a")["href"], b.find("a")["title"]
#                     locate = b.find("span", class_="t3").text
#                     salary = b.find("span", class_="t4").text
#                     item = {
#                         "href": href, "post": post, "locate": locate, "salary": salary
#                     }
#                     self.desc_url_queue.put(href)  # 岗位详情链接加入队列
#                     self.company.append(item)
#                 except Exception:
#                     pass
#         # 打印队列长度,即多少条岗位详情 url
#         logger.info("队列长度为 {} ".format(self.desc_url_queue.qsize()))
#
#     def post_require(self):
#         """
#         爬取职位描述
#         """
#         while True:
#             # 从队列中取 url
#             url = self.desc_url_queue.get()
#             resp = requests.get(url, headers=HEADERS)
#             if resp.status_code == 200:
#                 logger.info("爬取第 {} 条岗位详情".format(self.count))
#                 html = resp.content.decode("gbk")
#                 self.desc_url_queue.task_done()
#                 self.count += 1
#             else:
#                 self.desc_url_queue.put(url)
#                 continue
#             try:
#                 bs = BeautifulSoup(html, "lxml").find(
#                     "div", class_="bmsg job_msg inbox"
#                 ).text
#                 s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
#                     "\t", ""
#                 ).strip()
#                 with open(
#                     os.path.join("data", "post_require_new.txt"), "a", encoding="utf-8"
#                 ) as f:
#                     f.write(s)
#             except Exception as e:
#                 logger.error(e)
#                 logger.warning(url)
#
#     @staticmethod
#     def post_desc_counter():
#         """
#         职位描述统计
#         """
#         # import thulac
#         post = open(
#             os.path.join("data", "post_require.txt"), "r", encoding="utf-8"
#         ).read()
#         # 使用 thulac 分词
#         # thu = thulac.thulac(seg_only=True)
#         # thu.cut(post, text=True)
#
#         # 使用 jieba 分词
#         file_path = os.path.join("data", "user_dict.txt")
#         jieba.load_userdict(file_path)
#         seg_list = jieba.cut(post, cut_all=False)
#         counter = dict()
#         for seg in seg_list:
#             counter[seg] = counter.get(seg, 1) + 1
#         counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse=True)
#         pprint(counter_sort)
#         with open(
#             os.path.join("data", "post_pre_desc_counter.csv"), "w+", encoding="utf-8"
#         ) as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(counter_sort)
#
#     def post_counter(self):
#         """
#         职位统计
#         """
#         lst = [c.get("post") for c in self.company]
#         counter = Counter(lst)
#         counter_most = counter.most_common()
#         pprint(counter_most)
#         with open(
#             os.path.join("data", "post_pre_counter.csv"), "w+", encoding="utf-8"
#         ) as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(counter_most)
#
#     def post_salary_locate(self):
#         """
#         招聘大概信息，职位，薪酬以及工作地点
#         """
#         lst = []
#         for c in self.company:
#             lst.append((c.get("salary"), c.get("post"), c.get("locate")))
#         pprint(lst)
#         with open(
#             os.path.join("data", "post_salary_locate.csv"), "w+", encoding="utf-8"
#         ) as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(lst)
#
#     @staticmethod
#     def post_salary():
#         """
#         薪酬统一处理
#         """
#         mouth = []
#         year = []
#         thousand = []
#         with open(
#             os.path.join("data", "post_salary_locate.csv"), "r", encoding="utf-8"
#         ) as f:
#             f_csv = csv.reader(f)
#             for row in f_csv:
#                 if "万/月" in row[0]:
#                     mouth.append((row[0][:-3], row[2], row[1]))
#                 elif "万/年" in row[0]:
#                     year.append((row[0][:-3], row[2], row[1]))
#                 elif "千/月" in row[0]:
#                     thousand.append((row[0][:-3], row[2], row[1]))
#         pprint(mouth)
#
#         calc = []
#         for m in mouth:
#             s = m[0].split("-")
#             calc.append(
#                 (round((float(s[1]) - float(s[0])) * 0.4 + float(s[0]), 1), m[1], m[2])
#             )
#         for y in year:
#             s = y[0].split("-")
#             calc.append(
#                 (
#                     round(((float(s[1]) - float(s[0])) * 0.4 + float(s[0])) / 12, 1),
#                     y[1],
#                     y[2],
#                 )
#             )
#         for t in thousand:
#             s = t[0].split("-")
#             calc.append(
#                 (
#                     round(((float(s[1]) - float(s[0])) * 0.4 + float(s[0])) / 10, 1),
#                     t[1],
#                     t[2],
#                 )
#             )
#         pprint(calc)
#         with open(os.path.join("data", "post_salary.csv"), "w+", encoding="utf-8") as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(calc)
#
#     @staticmethod
#     def post_salary_counter():
#         """
#         薪酬统计
#         """
#         with open(os.path.join("data", "post_salary.csv"), "r", encoding="utf-8") as f:
#             f_csv = csv.reader(f)
#             lst = [row[0] for row in f_csv]
#         counter = Counter(lst).most_common()
#         pprint(counter)
#         with open(
#             os.path.join("data", "post_salary_counter1.csv"), "w+", encoding="utf-8"
#         ) as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(counter)
#
#     @staticmethod
#     def world_cloud():
#         """
#         生成词云
#         """
#         counter = {}
#         with open(
#             os.path.join("data", "post_pre_desc_counter.csv"), "r", encoding="utf-8"
#         ) as f:
#             f_csv = csv.reader(f)
#             for row in f_csv:
#                 counter[row[0]] = counter.get(row[0], int(row[1]))
#             pprint(counter)
#         file_path = os.path.join("font", "msyh.ttf")
#         wc = WordCloud(
#             font_path=file_path, max_words=100, height=600, width=1200
#         ).generate_from_frequencies(
#             counter
#         )
#         plt.imshow(wc)
#         plt.axis("off")
#         plt.show()
#         wc.to_file(os.path.join("images", "wc.jpg"))
#
#     @staticmethod
#     def insert_into_db():
#         """
#         插入数据到数据库
#         create table jobpost(
#             j_salary float(3, 1),
#             j_locate text,
#             j_post text
#         );
#         """
#         conn = pymysql.connect(
#             host="localhost",
#             port=3306,
#             user="root",
#             passwd="0303",
#             db="chenx",
#             charset="utf8",
#         )
#         cur = conn.cursor()
#         with open(os.path.join("data", "post_salary.csv"), "r", encoding="utf-8") as f:
#             f_csv = csv.reader(f)
#             sql = "insert into jobpost(j_salary, j_locate, j_post) values(%s, %s, %s)"
#             for row in f_csv:
#                 value = (row[0], row[1], row[2])
#                 try:
#                     cur.execute(sql, value)
#                     conn.commit()
#                 except Exception as e:
#                     logger.error(e)
#         cur.close()
#
#     def execute_more_tasks(self, target):
#         """
#         协程池接收请求任务,可以扩展把解析,存储耗时操作加入各自队列,效率最大化
#         :param target: 任务函数
#         :param count: 启动线程数量
#         """
#         for i in range(POOL_MAXSIZE):
#             self.pool.apply_async(target)
#
#     def run(self):
#         """
#         多线程爬取数据
#         """
#         self.job_spider()
#         self.execute_more_tasks(self.post_require)
#         self.desc_url_queue.join()  # 主线程阻塞,等待队列清空
#
#
# if __name__ == "__main__":
#     sys.setrecursionlimit(65535)
#     spider = JobSpider()
#
#     start = time.time()
#     spider.run()
#     logger.info("总耗时 {} 秒".format(time.time() - start))
#
#     # 按需启动
#     spider.post_salary_locate()
#     # spider.post_salary()
#     # spider.insert_into_db()
#     # spider.post_salary_counter()
#     # spider.post_counter()
#     spider.world_cloud()
