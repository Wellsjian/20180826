'''
字符串    列表list
'''

#需求 ，根据某些逻辑，拼接字符串
#0.123456789

str01 = ""
for item in range(10):
    #缺点： 每次 +  循环执行一尺就会产生新的对象替换str01变量存储的地址，之前的对象会被覆盖，成为垃圾；
    str01 += str(item)
print(str01)




name = "让我掉下眼泪的"
name1 = "不止作昨夜的酒"
name2 = "让我依依不舍的"
name3 = "不止你的温柔"

list = [name,name1,name2,name3]
str_result = " ".join(list)

print(str_result)










