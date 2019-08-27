"""
flag 扩展实例
"""

import  re

s = """
Hello
world
i am coming
please welcome me

北京
上海
张家口"""

#只能匹配到ASCLL
# regex = re.compile(r"\w+",flags=re.A)

#不区分大小写
# regex = re.compile(r[a-z]+",flags=re.I)

#使.可以换行
# regex = re.compile(r".+",flags=re.S)

#使^ $ 可以匹配到每一行的开头和结尾
# regex = re.compile(r"^北京",flags=re.M)
regex = re.compile(r"北京$",flags=re.M)

#为正则添加注释
pattern = """
\w+
\s+
\w+"""

l = regex.findall(s)
print(l)





