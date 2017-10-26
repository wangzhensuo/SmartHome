from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
sender_addr='wangzhensuo@163.com'
password='wangzhensuo'
to_addr='wangzhensuo@163.com'
smtp_server='smtp.163.com'

msg=MIMEText('测试邮件','plain','utf-8')
msg['From']=_format_addr('<%s>'% sender_addr)
msg['To']=_format_addr('<%s>'%to_addr)
msg['Subject']=Header('test','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.login(sender_addr,password)
server.sendmail(sender_addr,[to_addr],msg.as_string())
server.quit()
