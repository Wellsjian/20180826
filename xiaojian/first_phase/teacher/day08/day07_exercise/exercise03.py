"""
5. (扩展)将2 -- 100之间的素数存入列表（不用做成函数）.
素数：　只能被１和自身整除的数字
算法：判断从2开始到当前数字之间，是否存在可以被整除的数．
　　　如果存在则不是素数，如果不存在是素数
核心：该数字在从2　到　该数字　之间能否存在被整除的数
例如：2  3   5    7  8  9
 　　　6　能被2  整除
 　　　8　能被2  整除
      9 能被3  整除
"""

list_result = []
for item in range(2, 101):
  for number in range(2, item):
    if item % number == 0:
      # 不是素数
      break
  else:
    # 是素数
    list_result.append(item)

print(list_result)
