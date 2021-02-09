#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import threading
import time
import json
try:
    import queue
except ImportError:
    import Queue as q
# 添加线程  创建5个线程名
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
# 设置队列长度
workQueue = queue.Queue(300)
# 线程池
threads = []
start = time.time()
class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
 
    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
        print("Exiting " + self.name)
 
# 创建新线程
for tName in threadList:
    thread = myThread(tName, workQueue)
    thread.start()
    threads.append(thread)
 
 
 
def crawler(threadName, q):
    textmod = {}
    textmod = json.dumps(textmod)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    
#执行多线程
# 从队列里取出数据
    url = q.get(timeout=2)
    print(url)
 
# 读取数据，放入队列
count = 0
filename = 'id.txt'
f = open(filename, 'r').readlines()
for id in f:
    pid = id.replace("\"", "").replace("\n", "")
    count = count + 1
    # 生产index
    indexUrl = "https://www.baidu.com"
    url = indexUrl + '/aaa?id=' + pid 
    workQueue.put(url)
 
# 等待所有线程完成
for t in threads:
    t.join()
 
end = time.time()
print('Queue多线程批量执行时间为：', end - start)
#----------------------------------------------------
# -*- coding: utf-8 -*-
# (C) Guangcai Ren <renguangcai@jiaaocap.com>
# All rights reserved
# create time '2019/6/26 14:41'
import math
import random
import time
from threading import Thread

_result_list = []


def split_df():
    # 线程列表
    thread_list = []
    # 需要处理的数据
    _l = [i for i in range(100)]
    # 每个线程处理的数据大小
    split_count = 2
    # 需要的线程个数
    times = math.ceil(len(_l) / split_count)
    count = 0
    for item in range(times):
        _list = _l[count: count + split_count]
        # 线程相关处理
        thread = Thread(target=work, args=(item, _list,))
        thread_list.append(thread)
        # 在子线程中运行任务
        thread.start()
        count += split_count

    # 线程同步，等待子线程结束任务，主线程再结束
    for _item in thread_list:
        _item.join()


def work(df, _list):
    for i in _list:
        tmp = i + 100
        _result_list.append(tmp)


if __name__ == '__main__':
    split_df()
    print(len(_result_list), _result_list)
