"""
作业
1.三合一
2.每天练习独立完成
3.定义函数（扩展）:
        获取二维列表某个位置元素的 某个方向的 指定数量的所有元素
        例如： 获取下列二维列表   21位置元素  向右  指定个数 3 个

                00   01   02   03
                10   11   12   13
                20   21   22   23 ...
4.定义类：
        定义一个学生的类 ， 具有（姓名 性别  年龄  成绩）的数据
                        具有查找个人信息的行为
                定义函数  在学生列表中查找姓名是 无忌 的学生对象
                定义函数   在学生列表中查找 成绩 大于 60 的 所有 女 同学
                定义函数   计算成绩大于或等于60 的所有同学 数量
                定义函数   获取最高分的学生对象
                定义函数   删除所有低于60分的学生对象

        温馨提示;    不懂就画内存图

"""


class Students:

    def __init__(self, name, sex, score):
        self.name = name
        self.sex = sex
        self.score = score

    def print_student_info(self):
        print("姓名:%s 性别：%s 分数：%d" % (self.name, self.sex, self.score))


list = [
    Students("无忌", "男", 90),
    Students("赵敏", "女", 8),
    Students("周芷若", "女", 78),
    Students("青书", "男", 72),
    Students("张三丰", "男", 99),
    Students("阿狸", "女", 81),
    Students("金毛狮王", "男", 48),
]


def inquire_name(list_targe):
    for item in list_targe:
        if item.name == "无忌":
            return item


# re = inquire_name(list)
# re.print_student_info()

def inquire_score(list_targe):
    list01 = []
    for item in list_targe:
        if item.score >= 60 and item.sex == "女":
            list01.append(item)
    # return list01
    for item in list01:
        a = item.print_student_info()
    return a


re1 = inquire_score(list)


def inquire_pass_score(list_targe):
    count = 0
    for item in list_targe:
        if item.score >= 60:
            count += 1
    return count


re3 = inquire_pass_score(list)
print(re3)


def get_top_score(list_target):
    max = list_target[0].score
    for i in range(1, len(list_target)):
        if max < list_target[i].score:
            max = list_target[i].score
    for item in list_target:
        if item.score == max:
            return item


re5 = get_top_score(list)
re5.print_student_info()


def find_top_stident(list_target):
    for item in list_target:
        max(item.score)


def del_mot_pass_student(list_target):
    count = 0
    for item in range(len(list_target) - 1, -1, -1):
        if list_target[item].score < 60:
            del list_target[item]
            count += 1
    return list_target


del_mot_pass_student(list)


# for item in list:
#     item.print_student_info()

# 3.定义函数（扩展）:
#         获取二维列表某个位置元素的 某个方向的 指定数量的所有元素
#         例如： 获取下列二维列表   21位置元素  向右  指定个数 3 个  22   23
#
#                 00   01   02   03
#                 10   11   12   13
#                 20   21   22   23 ...


class Vctor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def print_list(n):
        list1 = []
        for i in range(n):
            list2 = []
            for j in range(n):
                list2.append("%s%s" % (i, j))
            list1.append(list2)

        return list1

    @staticmethod
    def move_left():
       return Vctor(0, -1)

    @staticmethod
    def move_right():
        return Vctor(0, 1)

    @staticmethod
    def move_up():
        return Vctor(-1, 0)

    @staticmethod
    def move_down():
        return Vctor(1, 0)


def get_elements(target, vect_pos, vect_dir, count):

    result = []
    for i in range(count):
        vect_pos.x += vect_dir.x
        vect_pos.y += vect_dir.y
        result.append(target[vect_pos.x][vect_pos.y])
    return result

list02 = Vctor.print_list(9)
print(list02)

print(get_elements(list02,Vctor(2,1),Vctor.move_up(),6))


