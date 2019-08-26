"""
作业
"""
import re

def get_address():
    obj = open("1.txt")
    data = obj.read()
    l = re.split(r"\n\n",data)
    dict01 = {}
    for i in l:
        m = re.search(r"^\S+",i).group()
        n = re.findall(r"address is \S+",i)
        for j in n:
            s = re.findall(r"\d+\S+",j)
            dict01[m] = s
    return dict01

def find_port(port):
    dict = get_address()
    return dict[port]


print(find_port("Null0"))












