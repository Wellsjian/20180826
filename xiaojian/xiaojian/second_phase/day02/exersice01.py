"""
练习
    一段文字，在文字中可能出现括号配对错误的情况
    要求写一段代码，检测这段文字中是否出现括号错误
    括号包括 {} [] ()
"""

from day02.s_stack import SStack

parents = "()[]{}"

list01 = ["(", "[", "{"]
dict01 = {"}": "{", ")": "(", "]": "["}
st = SStack()


# 负责提供遍历的括号
def parent(text):
    """
    遍历字符串，只提供括号字符和其位置
    :return:
    """
    i, text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parents:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


# 字符匹配的验证工作
def ver():
    for text_ele, item in parent(text):
        if text_ele in list01:
            st.push((text_ele, item))
        elif st.is_empty() or st.pop()[0] != dict01[text_ele]:
            print("%d位置的%s元素出错了" % (item, text_ele))
            break
    else:
        if st.is_empty():
            print("全部匹配")
        else:
            p = st.pop()
            print(p[0], p[1])


text = "daf{(s)d}ffds[fw]efsdf asdsa(f)ds)afsafsafsaf"
ver()
