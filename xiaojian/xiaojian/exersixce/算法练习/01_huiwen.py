
# 一个数的十进制 二进制 以及 八进制 正序和倒序相等

import re
def get_number():
    number = 11
    while True:
        bin1 = re.findall(r"\d+",bin(number))[1]
        oct1 = re.findall(r"\d+",oct(number))[1]
        number = str(number)
        if number == number[::-1] and bin1 == bin1[::-1] and oct1 == oct1[::-1]:
            return int(number)
        number = int(number) + 2
print(get_number())
