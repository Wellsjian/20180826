# 　练习：定义函数，计算指定范围内的素数
"""
def get_prime(begin,end):
  list_result = []
  for item in range(begin, end):
    for number in range(2, item):
      if item % number == 0:
        # 不是素数
        break
    else:
      # 是素数
      list_result.append(item)
  return list_result

print(get_prime(2,100))
"""


def is_prime(target_number):
  """
    判断目标数字是否是素数
  :param target_number: 需要判断的数字
  :return: ｔｒｕｅ是素数，ｆａｌｓｅ不是素数
  """
  if target_number <= 1:
    return False
  for number in range(2, target_number):
    if target_number % number == 0:
      return False
  return True


def get_prime(begin, end):
  """
    获取指定范围内的素数
  :param begin: 开始值(包含)
  :param end: 结束值(不包含)
  :return:
  """
  # list_result = []
  # for item in range(begin, end):
  #   if is_prime(item):
  #     list_result.append(item)
  # return list_result
  return [item for item in range(begin, end) if is_prime(item)]





