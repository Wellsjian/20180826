# 例如 351 = 3*51 = 153
#     621 = 6*21 = 126
# 在1000 - 9999 中寻找相同规律的数
#  逆波兰表示法 ;31- 表示的是3-1
#                 34*5- 表示的是3*4-5
#         思想即为栈操作,数字进栈,遇到操作符出栈,计算 ,结果在入栈
def get():
    op = ["+","-","*","/",""]
    for i in range(1000,10000):
        number1 = str(i)
        if "0" not in number1:
            for j in op:
                for k in op:
                    for l in op:
                        val = number1[3] + j + number1[2] + k + number1[1] + l + number1[0]
                        if (j != "" or k != "" or l != "") and i == eval(val):
                            print(val, "=", i)

get()


