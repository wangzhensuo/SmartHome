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
