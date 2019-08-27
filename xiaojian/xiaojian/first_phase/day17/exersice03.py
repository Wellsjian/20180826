"""
定义函数，在控制台中获取成绩1--100
如果输入错误，重新输入
"""
def get_score():
    while True:
        try:
            score = int(input("请输入您的成绩："))

        except:
            continue

        if 0 <= score <= 100:
            return score

print(get_score())














