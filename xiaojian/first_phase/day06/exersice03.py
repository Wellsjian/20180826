# 在控制台中选取季度，并将相应月份打印出来

# season = input("请输入季度：")

# if season == "春":
#     print("该季度有1 2 3 月份")
# elif season == "夏":
#     print("该季度有4 5 6 月份")
# elif season == "秋":
#     print("该季度有7 8 9 月份")
# elif season == "冬":
#     print("该季度有10 11 12 月份")
# else:
#     print("您的输入不合法")


season = input("请输入季度：")

season_dict = {"春": (1, 2, 3),
               "夏": (4, 5, 6),
               "秋": (7, 8, 9),
               "冬": (10, 11, 12)
               }


if season in season_dict:
    print(season_dict[season])
else:
    print("输入不正确")
