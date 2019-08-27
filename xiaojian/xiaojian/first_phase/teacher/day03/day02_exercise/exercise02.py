"""
4. 在控制台中录入圆形的半径
   计算面积(3.14 * r 平方)与周长(2 * 3.14 * r)
"""
radius = float(input("请输入圆形半径:"))
area = 3.14 * radius **2
length = 2 * 3.14 * radius
# 四舍五入,保留指定精度的小数.
length = round(length,3)
print("面积是:"+str(area)+",周长是:"+str(length))