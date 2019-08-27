import random
import itertools

# m = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and j != k and i != k:
#                 print('%d%d%d' % (i, j, k))
#                 m += 1
#
# print(m)
s = "1234"
l = itertools.permutations(s, 3)
l = list(l)
a = len(l)
print(l)
print(a)
