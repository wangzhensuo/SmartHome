#coding=utf8
import requests
import itchat
'''
生活百科,图片搜索,数字计算,问答百科,知识库,中英互译,聊天对话,
笑话大全,故事大全,成语接龙,新闻资讯,星座运势,脑筋急转弯,歇后语,绕口令,顺口溜,   
天气查询,菜谱大全,快递查询,列车查询,日期查询,附近餐厅,附近酒店,实时路况,果蔬报价,汽油报价,股票查询,城市邮编
'''
KEY = '71f28bf79c820df10d39b4074345ef8c'#'71f28bf79c820df10d39b4074345ef8c'

def get_response(msg):
    print("=======1======")
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data, verify=False).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
#@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = "你慢点说，当前网络不好"
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg)
    print(reply)
    return reply or defaultReply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
if __name__=="__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()

