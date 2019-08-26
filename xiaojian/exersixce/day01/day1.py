import numpy as np

arry01 = np.array([1,2,3,4,5])
print(arry01)
arry02 = np.array([2,2,3,5,5])
print(arry02)
arry03 = arry01 + arry02
print(arry03)
array04 = arry02 - arry01
print(array04)
array05 = arry02 * arry01
print(array05)

# 数组的创建
a = np.arange(0,5,1)
print(a)
z = np.zeros(10)
o = np.ones(10)
print(z)
print(o)

b = np.array([[1,2],[3,4],[5,6]])
print(b)
print(np.zeros_like(b))
print(np.ones_like(b))

# ndarray.shape  数组维度
# ndarray.dtype  元素类型
# ndarray.size len(ndarray) 元素的个数

c = np.arange(1,9)
c.shape = (2,2,2)
print(c)
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k],end="")

# 设置dtype方式
print()

data = [
    ("zs",[60,61,65,],15),
    ("ls",[64,66,68],16),
    ("www",[64,68,67],17)
]

c = np.array(data,dtype={
    "name":['name','score','age'],
    'formats':['U2','3int32','int32']
})

b = np.array(data,dtype=[
    ('name','str',2),
    ('scores','int32',3),
    ('age','int32',1)
])
print(b)
a = np.array(data,dtype="U10,3int32,int32")
print(a,a[1]["f1"])
