#!/usr/bin/env python3
# -*- coding: utf-8
import re
import pymysql
import csv
import time
import requests
import multiprocessing
import random
from bs4 import BeautifulSoup
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET CLR 1.1.4322)',
]
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
#     'Connection': 'keep-alive',
# }

data_count =0
def get_index_url(url):
    header = {
        'User-Agent': user_agent_list[random.randint(0,5)],
        'Connection': 'keep-alive',
    }

    wbdata = requests.get(url, headers=header).content
    soup = BeautifulSoup(wbdata, 'html.parser', from_encoding="GBK")
    links = soup.select('html > body > div.dw_wp > div > div.el > p.t1 > span > a')
    time.sleep(1)
    for link in links:
        try:
            db = pymysql.connect(host='localhost', port=3307, user='root', password='usbw', db='test', charset='utf8')
            cur = db.cursor()
            global data_count
            data_count = data_count + 1
            print('第' + str(data_count) + '子页面')
            page_url = link.get('href')
            wbdata2 = requests.get(page_url, headers=header).content
            soup2 = BeautifulSoup(wbdata2, 'html.parser',from_encoding="GBK")
			company_info = "NONE"
            company_info = soup2.select('html > body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > p.msg.ltype')[0].text.strip().replace(" ", "").replace(' ', '').replace("\t", "").replace("\r", "").replace(",",".").replace('\'','')
            print("======================"+company_info+"=================")
            company_cate_list = company_info.split('|')
            company_kind = company_cate_list[0]
            company_scale = company_cate_list[1]
            company_industry = company_cate_list[2]
            print(company_kind,company_scale,company_industry)
			
            job_name = "NONE"
            job_name = soup2.select(
                'html > body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div.in > div.cn > h1')[0].text.strip().replace("\n", "").replace(' ', '').replace("\t", "").replace("\r", "").replace(",",".").replace('\'','')

            gongzi = "NONE"
            gongzi = soup2.select(
                'html > body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > strong')[0].text
            jieshao = "NONE"
            jieshao = soup2.select(
                'html > body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div.tBorderTop_box > div.bmsg.job_msg.inbox')[0].text.strip().replace("\n", "").replace(' ', '').replace("\t", "").replace("\r", "").replace(",",".")

            company_name='NONE'
            company_name = soup2.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > p.cname > a')[0].text.strip().replace("\n", "").replace(' ', '').replace("\t", "").replace("\r", "").replace(",",".")

            company_addr='NONE'
            #body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(3) > div > p
            company_addr = soup2.select('.fp')[-1].text.strip().replace("\n", "").replace(' ', '').replace("\t", "").replace("\r", "").replace(",",".")
        except:
            print("not found!"+page_url,company_name,company_addr,gongzi)
            with open("C:/log.csv", 'a', encoding='utf-8') as f:
                f.write("not found!"+','+page_url+','+company_name+','+company_addr+','+gongzi+'\n')
            pass

        print('----------1-----')
        gongzi_p = str2float(gongzi)
        gongzi_min=str(gongzi_p[0])
        gongzi_max = str(gongzi_p[1])
        job_url = page_url
        job_info = jieshao.replace('\'','')
        print('------2---------')
        data_id=re.findall("\d+",job_url)[1]
        print(data_id)
        sql_insert = """insert into dalianjob(data_id,job_name,company_name,company_addr,gongzi_min,gongzi_max,job_url,job_info) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(
            data_id,job_name, company_name, company_addr, gongzi_min, gongzi_max, job_url, job_info)
        print('------3---------')
        # time.sleep(1)
        cur.execute(sql_insert)
        print('------4---------')
        print(job_name,company_name,company_addr,gongzi_min,gongzi_max,job_url,job_info)
        db.commit()
        print('------5---------')
        cur.close()
        db.close()
        print('------6---------')
        # with open("C:/data.csv", 'a', encoding='utf-8') as f:
        #     try:
        #         # print('---------w--')
        #         f.write(job_name.replace(",","."))
        #         f.write(',')
        #         f.write(company_name.replace(",","."))
        #         f.write(',')
        #         f.write(company_addr.replace(",","."))
        #         f.write(',')
        #         gongzi_p = str2float(gongzi)
        #         f.write(str(gongzi_p[0]))
        #         f.write(',')
        #         f.write(str(gongzi_p[1]))
        #         f.write(',')
        #         f.write(page_url.replace(",","."))
        #         f.write(',')
        #         f.write(jieshao.replace(",","."))
        #         f.write("\n")

            # except:
            #     print("error!!!")
            #     print((job_name, gongzi, page_url, url, jieshao))
            #     pass

def str2float(str_data):
    # str_data="2.5-3千/月"
    gz = re.findall("(\d.*\d*)-(\d.*\d*)千", str_data)
    if not gz:
        min_gz = 0
        max_gz = 0
        gz_w = re.findall("(\d.*\d*)-(\d.*\d*)万", str_data)
        if not gz_w:
            min_gz = 0
            max_gz = 0
        else:
            min_gz = float(gz_w[0][0]) * 10000
            max_gz = float(gz_w[0][1]) * 10000
    else:
        min_gz = float(gz[0][0]) * 1000
        max_gz = float(gz[0][1]) * 1000
    return min_gz, max_gz


if __name__ == "__main__":
    try:
        pool = multiprocessing.Pool(processes=8)
        for i in range(1, 1105):
            url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=230300%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keywordtype=2&curr_page=" + str(
                i)
            pool.apply_async(get_index_url, (url,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    except:
        print('abort')
