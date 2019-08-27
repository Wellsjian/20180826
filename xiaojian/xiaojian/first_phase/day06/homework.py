# 1.三合一
# 2.当天练习独立完成
# 3.1970-2050年中的闰年，存入列表

# list_year=[]
# for year in range(1970,2050):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         list_year.append(year)
#     else:
#         continue
# print(list_year)
#
# list_year=[]
# list_year= year for year in range(1970,2050) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:

# 4.【1】描述多个商品信息   屠龙刀，10000元  倚天剑，10000元   打狗棒，5000元

# dict_message={}
# while  True:
#      dict_attribute={}
#      name=input("请输入商品名称：")
#      if name =="":
#          break
#      while True:
#          attribute=input("请输入商品属性：")
#          if  attribute=="":
#              break
#          price=input("请输入商品属性值：")
#          dict_attribute[attribute]=price
#      dict_message[name]=dict_attribute
# for key1,value1 in dict_message.items():
#     print("%s： "%(key1,),end=" ")
#     for key,value in value1.items():
#         print("%s：%s"%(key,value),end=" ")


# .【1】存储全国各个城市景区，美食信息   北京：景区：故宫，天坛,天安门 美食：烤鸭，豆汁儿
# 四川：景区：九寨沟 峨眉，春熙路 美食：火锅，串串香，兔头
'''{北京：
{景区":["故宫","天坛","天安门"]}
{"美食"：["烤鸭,"豆汁]}
}
'''
dict_area = {}
while True:
    dict_spot = {}
    area = input("请输入地区：")
    if area == "":
        break
    while True:
        dict_attributes = []
        spot = input("请输入类型：")
        if spot == "":
            break
        while True:
            attributes = input("请输入特点：")
            if attributes == "":
                break
            dict_attributes.append(attributes)
            # attributes_value = input("请输入特点为：")
            # dict_attributes[attributes] = attributes_value
        dict_spot[spot] = dict_attributes
    dict_area[area] = dict_spot

for key, value in dict_area.items():
    print("%s: " % (key), end=" ")
    for key1, value1 in value.items():
        print("%s特色是%s" % (key1, value1), end=" ")
        for attributes in value1:
            print("%s" % (value1), end=" ")
# 5.计算一个字符串中的字符，以及出现的次数
'''{
  a:2
  b:1
  c:3  
}
逐一判断字符出现的次数
'''
# dict_result={}
# str_input="abcdefabdsfgexcvwea"
# for i in str_input:
#     #该字符在字典中不存在，新增字符增1
#     if i not in dict_result:
#         dict_result[i]=1
#         #该字符存在，累加次数加1
#     else:
#         dict_result[i]+=1
# print(dict_result)



# 6.猜拳游戏  系统随机选择，用户输入，判输赢
# import random
# dict_win={
#     "石头":"剪刀",
#     "剪刀":"布",
#     "布":"石头",
# }
# #电脑随机出
# list01=["石头","剪刀","布"]
# sys_input=random.randint(0,2)
# str_sys_input=list01[sys_input]
#
# print(str_sys_input)
#
# str_user_input=input("请输入：")
# if str_sys_input==str_user_input:
#     print("平局")
# elif str_user_input in dict_win:
#     print("赢")
# else:
#     print("输")
# 7.阅读 pyhton 6章字典
