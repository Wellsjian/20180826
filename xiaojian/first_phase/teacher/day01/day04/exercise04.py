# 练习1: 格式化字符串:
# 在控制台中按照如下格式输出:  圆形的面积是52.5,周长是35.25.
# 其中图形是变量,面积与周长的值是变量.
graph = "圆形"
area = 52.5
length = 35.25
msg = "%s的面积是%.1f,周长是%.2f." % (graph, area, length)
print(msg)

# 练习2: 在控制台中显示120秒的倒计时.02:00 --> 01:59 ....
for second in range(120, -1, -1):
  print("%02d:%02d" % (second // 60, second % 60))

# 16:50 上课