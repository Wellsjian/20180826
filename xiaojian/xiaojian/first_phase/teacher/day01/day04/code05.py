"""
  字符串--通用操作
  练习:exercise05.py
  练习:exercise06.py
"""

str01 = "苏大强"
str02 = "苏明玉"
# 拼接
str01 += str02
print(str01)

# 重复生成元素
str02 *= 2
print(str02)

# 依次比较两个容器中元素,一但不同则返回比较结果
print("aec" > "abf")

# 成员运算
print("大苏" in str01)

# 索引
str02 = "我叫苏大强"
print(str02[1])#叫
print(str02[-1])#强
# 切片
print(str02[0:3])# 我叫苏
print(str02[2:5])# 苏大强
# 开始索引　默认为头
print(str02[:3])# 我叫苏
# 结束索引　默认为尾
print(str02[2:])# 苏大强
# 获取全部
print(str02[:])# 苏大强
print(str02[::2]) # 我苏强
print(str02[::-1]) # 强大苏叫我
print(str02[-2:-4:-1])# 大苏
print(str02[3:1:-1])# 大苏
# 可以同时使用正向和反向索引值
print(str02[3:-4:-1])# 大苏

print(str02[1:1])# 空
print(str02[3:1])# 空
print(str02[-2:1])# 空














