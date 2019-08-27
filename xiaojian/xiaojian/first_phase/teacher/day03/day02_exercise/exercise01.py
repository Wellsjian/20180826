"""
3. 温度转换器
摄氏度 = (华氏度 - 32) / 1.8
华氏度 = 摄氏度 * 1.8 +32
开氏度 = 摄氏度 + 273.15
"""

# fahrenheit = input("请输入华氏度:")
# fahrenheit = float(fahrenheit)
# centigrade = (fahrenheit - 32) / 1.8
# print("摄氏度是:"+str(centigrade))

# centigrade = float(input("请输入摄氏度:"))
# fahrenheit = centigrade * 1.8 + 32
# print("华氏度是:"+str(fahrenheit))

centigrade = float(input("请输入摄氏度:"))
kelvin = centigrade + 273.15
print("开氏度是:"+str(kelvin))




