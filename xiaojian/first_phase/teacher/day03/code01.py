"""
  行
"""

# 3个物理行 3个逻辑行
a = 1
b = 2
c = a + b

# 1个物理行 3个逻辑行
a = 1;
b = 2;
c = a + b

# 3个物理行 1个逻辑行
d = a + \
    b + \
    c

# 隐式换行
d = (a + b +
     c)