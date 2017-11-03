
import requests
from bs4 import BeautifulSoup


page_url = 'http://creditease.51job.com/sc/show_job_detail.php?jobid=92335524'#'http://jobs.51job.com/dalian/95618446.html?s=01&t=0'
# page_url='http://jobs.51job.com/dalian/95618446.html?s=01&t=0'
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 3.0.04506)',
    'Connection': 'keep-alive',
}
wbdata2 = requests.get(page_url, headers=header).content
soup = BeautifulSoup(wbdata2, 'html.parser',from_encoding="GBK")
job_name = soup.select('html > body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div > div > p')[0].text
company_name = soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > p.cname > a')[0].text
company_addr = soup.select('.fp')[-1].text

# print(job_name)
print(company_addr)
# print(company_name)