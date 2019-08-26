# 练习:在控制台中获取季度,显示该季度有多少月份.
#     春  -->  1  2  3
#     夏  -->  4  5  6
#     秋  -->  7  8  9
#     冬  -->  10 11 12

# season = input("请输入季度:")
# if season == "春":
#   print("1  2  3")
# if season == "夏":
#   print("4  5  6")
# if season == "秋":
#   print("7  8  9")
# if season == "冬":
#   print("10 11 12")

# 方法１：
# season = input("请输入季度:")
# dict_seasons = {
#   "春":"1  2  3",
#   "夏":"4  5  6",
#   "秋":"7  8  9",
#   "冬":"10 11 12"
# }
# if season in dict_seasons:
#   print(dict_seasons[season])
# else:
#   print("输入错误")

# 方法2:　　　　15:30 上课
season = input("请输入季度:")
dict_seasons = {
  "春": (1, 2, 3),
  "夏": (4, 5, 6),
  "秋": (7, 8, 9),
  "冬": (10, 11, 12)
}
if season in dict_seasons:
  # 根据季度获取所有月
  months = dict_seasons[season]
  for item in months:
    print(str(item) + "月份")
else:
  print("输入错误")
