import pymongo
# pymongo 是跟 MongoDB 连接的库，引用的前提是已经安装了 MongoDB

client = pymongo.MongoClient('localhost',27017)    # 激活MongoDB
walden = client['walden']                          # 创建工作簿 walden
sheet_tab = walden['sheet_tab']                    # 创建工作表 sheet_tab

path = 'C:\walden.txt'
with open(path,'r') as f:
    lines = f.readlines()
    for index,line in enumerate(lines):
        data = {
            'index':index,
            'line':line,
            'words':len(line.split())
        }
        sheet_tab.insert_one(data)                 # 向工作表里逐行添加内容

# for item in sheet_tab.find({'words':0}):
#     print(item)
for item in sheet_tab.find():
    print(item['line'])

