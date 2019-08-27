# 在控制台中选取季度，并将相应月份打印出来

season = input("请输入季度：")

if season == "春":
    print("该季度有1 2 3 月份")
elif season == "夏":
    print("该季度有4 5 6 月份")
elif season == "秋":
    print("该季度有7 8 9 月份")
elif season == "冬":
    print("该季度有10 11 12 月份")
else:
    print("您的输入不合法")
