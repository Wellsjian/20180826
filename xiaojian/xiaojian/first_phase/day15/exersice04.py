"""
练习，实现其他类型的运算符
"""

class Victor:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other
    def __radd__(self, other):
        return self.x + other
    def __iadd__(self, other):
        self.x += other
        return self
    def __imod__(self, other):
        self.x %= other
        return self
    # def __sub__(self, other):
    #     return self.x -other
    # def __mul__(self, other):
    #     return self.x * other
    # def __truediv__(self, other):
    #     return self.x / other


v1 = Victor(2)
re = v1 + 3

print(re)
re = 1 + v1
print(re)

v1 += 6
print(v1.x)

v1%=2
print(v1.x)
