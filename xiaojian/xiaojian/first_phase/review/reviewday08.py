"""
  day08 复习
  函数
    1. 定义: 一个/单一        的功能
    2. 语法:
                def 函数名(形式参数):
                    文档字符串
                    函数体
                    return 数据
            -------------------------------
                函数名(实际参数)
                变量 = 函数名(实际参数)

       -- 参数:要求调用者必须提供的信息.
               根据形参传递的信息.
       -- 返回值:函数定义者告诉调用者的结果
    3. 作用:代码复用    维护性高(结构清晰)
    3. 参数:
      实际参数:
        -- 位置传参:实参与形参一一对应
          -- 序列传参:用*拆解序列(字符串/列表/元组)的元素
        -- 关键字传参:实参根据形参名称对应
          -- 字典传参:用**拆解字典的记录

      形式参数:
        -- 默认/缺省参数:实参在不传递的情况下,使用默认值代替.
        -- 位置形参:
          -- 星号元组形参:将位置实参包装为一个元组
                       可以传递无限个位置实参
        -- 命名关键字形参:要求实参必须使用关键字传递.
          -- 双星号字典形参:将关键字实参包装为一个字典
                          可以传递无限个关键字实参
"""


def fun01(a, b, c):
  pass


num01, num02, num03 = 1, 2, 3
# 位置
fun01(num01, num02, num03)
# 序列传参
list01 = [3, 4, 5]
fun01(*list01)

# 关键字传参
fun01(b="B", a="A", c="C")


# 默认/缺省形参
def fun02(a=0, b=0, c=0):
  pass


# 关键字传参 + 缺省形参 : 随意传参
fun02(b="B")


def fun03(list_target=[]):
  list_target.append("a")
  print(list_target)
  print(id(list_target))


fun03([1, 2, 3])  # "a"
# ...............
fun03()  # "a"
# .................
fun03()  # "a" ,"a"
# 注意:66行调用函数fun03使用的列表对象与68行调用函数使用的是一个.
# 每次调用后的结果,都影响以后的调用.
# 结论:默认参数,建议不要使用在可变对象中

dict01 = {"b": "B", "c": "C", "a": "A"}
fun01(**dict01)


def fun04(*args):
  pass

fun04()
fun04(3,54,5,6,7)

# 命名关键字形参
def fun05(*args,a):
  pass

fun05(1,2,a = 1)

# 双星号字典形参
def fun06(**kwargs):
  pass

fun06(a=1,b=2)