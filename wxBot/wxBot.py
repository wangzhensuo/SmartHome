from wxpy import *
import csv
import led
import tuling
import ssl
import random
kefu=['周芷若',’小昭‘，’赵敏郡主‘，’木婉清‘，’如花‘，’如月‘，‘秋香’]
addfriend_request = '加好友'  #自动添加好友的条件
admin_request_name = '改成自己的'    #定义管理员微信名（必须是机器人的好友）  ps：raw_content字段需要自己手动更改微信名，微信号
admin_request_num = '改成自己的'   #定义管理员微信号（必须是机器人的好友）
invite_text = "您好呀!我是智能管家，暂时有如下功能：\n 回复“开灯”： 开灯\n 回复“关灯”：关灯\n 回复“陪聊”：进入智能聊天模式 \n 回复“退出陪聊”：退出智能聊天模式" 
tulingFunc = "生活百科, 图片搜索, 数字计算 , 中英互译, 聊天对话, \
笑话故事, 成语接龙, 新闻资讯, 星座运势, 天气查询, 菜谱大全,快递查询,列车查询,餐厅酒店,实时路况,果蔬报价,汽油报价,股票查询,城市邮编"

chat_mode = 0
#invite_text = "您好呀!回复'功能 + 数字'获取对应功能\n1.我要加群\n2.我要加入协会\n3.我要购买鞋子\n4.了解我们\n5.我需要帮助\n例如：要获取我要加群的功能时回复\n\n功能1"  #任意回复获取的菜单
#group_name = '测试群'    #定义要查找群的名字
menu_1 = '功能1'   #菜单选项1 定义加群的条件
menu_2 = '功能2'  #菜单选项2
menu_3 = '功能3'  #菜单选项3
menu_4 = '功能4'  #菜单选项4  
menu_5 = '功能5'  #菜单选项5 
csv_1 = 'test.csv'   #表格1


bot = Bot(cache_path = True)
bot.enable_puid()  #启用聊天对象的puis属性
#adminer = bot.friends(update=True).search(admin_request_name)[0]
#my_group = bot.groups(update=True).search(group_name)[0] #wq
#group_admin = my_group.members.search(admin_request_name)[0]


admin_puids = frozenset(['XX', 'YY'])   #不可变集合
admins = list(map(lambda x: bot.friends().search(puid=x), admin_puids))

def invite(user):
    groups = sorted(bot.groups(update=True).search(group_name),
                    key=lambda x: x.name)   #sorted用于排序，lambda x:x.name用于群名排序
    if len(groups) > 0:
        for group in groups:
            if len(group.members) == 500:
                continue    
            if user in group:
                content = "您已经加入了{} [微笑]".format(group.nick_name)   #经过format格式化的内容传递到{}
                user.send(content)
            else:
                group.add_members(user, use_invitation=True)
            return
        else:
            next_topic = group_tmpl.format(re.search(r'\d+', s).group() + 1)  #当前群的名字后面+1
            new_group = bot.create_group(admins, topic=next_topic)
            #以上3句代码的解释为：利用for if else语句进行判断，如果从查找的群名里面找不到对应的群就自动创建一个新群并添加进去
    else:
        print('Invite Failed')

#写表函数
def table(user, text):
    #提取用户的文本，把有用的写入表里
    msg_text = text
    tables = msg_text.split('\n')
    table_name = tables[1].split(':')[1]
    table_stu_num = tables[2].split(':')[1]
    table_phone_num = tables[3].split(':')[1]
    table_department = tables[4].split(':')[1]
    table_list = [table_name, table_stu_num, table_phone_num, table_department, '等待缴费']
    user.send('请稍等，后台处理中')
    with open(csv_1, 'r') as f:   #检查表里是否有登记的学号
        fr_csv = csv.reader(f)
        for row in fr_csv:
            if table_stu_num in row:
                user.send('报名失败，该学号已经登记过了')
                break
        else:
            with open(csv_1, 'a') as f:          #写入表
                fw_csv = csv.writer(f)
                fw_csv.writerow(table_list)
            with open(csv_1, 'r') as f:          #查看是否写入成功
                fr_csv = csv.reader(f)
                for row in fr_csv:
                    if table_stu_num in row:
                        user.send('报名成功,请回复‘支付宝’或者‘微信’进行支付')
                        break
                else:
                    user.send('报名失败，请重新报名或者联系管理员')

#查询表函数
def check(user, text):
    check_text = text.split(':')[1]
    with open(csv_1, 'r') as f:
        fr_csv = csv.reader(f)
        for row in fr_csv:
            if check_text in row:
                user.send('登记信息如下，如有疑问请联系管理员')
                user.send('学号:'+row[1]+"\n缴费情况:"+row[-1])
                break
        else:
            user.send('暂无学号登记记录')   

# 注册好友请求类消息
@bot.register(msg_types=FRIENDS,enabled=True)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    #if addfriend_request in msg.text.lower():#去掉好友验证
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('机器人自动接受了你的请求,你可以任意回复获取功能菜单，若机器人没回复菜单则表明机器人尚未工作，请等待')

#注册自动回复好友消息
@bot.register(Friend, msg_types=TEXT)
@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):

    global chat_mode
    #'''
    if '陪聊' in msg.text:
        print("----开始陪%s聊天-----"% msg.sender.nick_name)
        chat_mode = 1
        msg.sender.send(msg.sender.nick_name+"呀，欢迎与’+kefu[random.randon(1,8,1)]+‘进入智能聊天模式")
        msg.sender.send("我可以查以下信息：\n"+tulingFunc)
    if '退出' in msg.text:
        chat_mode = 0
        msg.sender.send("退出智能聊天模式")
        print("----退出与%s聊天-----"% msg.sender.nick_name)
    if chat_mode == 1:
        tulingRly=tuling.tuling_reply(msg)
        msg.sender.send(tulingRly)
        print("---6------")
        return
    #'''
    if '开灯' in msg.text and chat_mode ==0:
        led.turnOnLed()
        print("-----5----")
        msg.sender.send('已开灯 ,'+msg.sender.nick_name)
        print()
        #msg.sender.send_image("biying.jpg", media_id=None)
    elif '关灯' in msg.text and chat_mode ==0:
        led.turnOffLed()
        print("-----6----")
        msg.sender.send('已关灯')
    elif msg.text and chat_mode ==1:
        tulingRly=tuling.tuling_reply(msg)
        msg.sender.send(tulingRly)
    else:
        return msg.sender.nick_name+"\n"+invite_text 

#处理管理员信息
'''
@bot.register(adminer, msg_types=TEXT)
def adminer(msg):
    print(msg.text)
    if '备份' in msg.text:
        msg.sender.send_file('test.csv')
    else:
        return "请检查命令是否输入正确"    
'''
#群聊管理
'''
@bot.register(my_group, msg_types=TEXT)
def group(msg):
    if msg.is_at :
        if '踢出' in msg.text:
            if msg.member == group_admin :
                for member_name in msg.text.split('@')[2:]:
                    print(member_name)
                    re_name = my_group.members.search(member_name)[0].remove()
                    print(re_name)
                    msg.sender.send("已经移出:"+member_name)
            else:
                return "你不是管理员不能进行踢人操作"
        else:
            xiaoi.do_reply(msg)  
'''   
bot.join()


