"""
练习
    从终端输出一个单词，打印出单词的解释
    如果没有该单词，打印“没有该单词”
"""

def get_dict(targrt):
    obj = open("./dict.txt", "r+")

    for line in obj:

        result = line.split(" ")[0]
        # result = ""
        # for i in obj.readline():
        #     result += i
        #     if i == " ":
        #         break
        if result > targrt:
            print("没有找到该单词")
            break
        if targrt == result:
            # print(line)
            # break
            return line
    else:
        print("没有找到该单词")


# get_dict("money")


























