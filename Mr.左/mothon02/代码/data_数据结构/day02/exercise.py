# 练习：检测一段文字中的括号是否为成对出现，如果不是则报出括号匹配的错误问题
from sstack_栈的顺序存储结构 import *
text = """ The [globals] argument is (only used to) determine the (context);
    they are not modified.  The locals {argument is unused}. 
    """
parens = "()[]{}"  # 验证的括号
left_parens = "([{"
opposite = {')': '(', ']': '[', '}': '{'}  # 对应关系


def parent(text):
    # 记录字符串索引
    i, text_len = 0, len(text)
    while True:
        # 逐个遍历字符串，如果没有到结尾且不是括号，就会继续向后遍历
        while i < text_len and text[i] not in parens:
            i += 1

        if i >= text_len:
            return
        else:
            yield text[i], i  # 生成括号字符和对应位置
            i += 1


st = SStack()  # 初始化一个栈
for pr, i in parent(text):
    if pr in left_parens:
        st.push((pr, i))  # 将左括号及其位置入栈
    elif st.is_empty() or st.pop()[0] != opposite[pr]:  # or 有短路原则　　如果是右括号
        print("Unmatching is found at %d for %s" % (i, pr))
        break
    else:
        # 　循环正常结束，判断栈是否为空
        if st.is_empty():
            print("All parentheses are matched")
        else:
            # 有左括号没有匹配
            e = st.pop()
            print("Unmatching is found at %d for %s" % (e[1], e[0]))
# All parentheses are matched
# All parentheses are matched
# All parentheses are matched
# All parentheses are matched