# import re
# def number(num):
#     number1 = str(num)
#     list = []
#     while len(number1) != 0:
#         res = re.search(r"\d+", number1).group()
#         for i in range(len(res) - 1, -1, -1):
#             list.append(res[i])
#         res1 = "".join(list)
#         if number1[0] == "-":
#             res2 = "-" + res1
#             return int(res2)
#         else:
#             return int(res1)
#
# print(number(-150))

s = 't dafas fds  vb ad'
print(len(s))
s1 = ''
for i in range(len(s)):
    if s[i] != " ":
        s1 += s[i]
    else:
        s1 += "*"
print(s1)