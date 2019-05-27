#1.
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],]
#1.
import exercise01
n01=exercise01.DoubleListHelper.get_elements(list01, exercise01.Vector2(1, 0), exercise01.Vector2.right(), 3)
print(n01)
#2.
from exercise01 import DoubleListHelper as helper
from exercise01 import Vector2 as vect
re=helper.get_elements(list01, vect(1, 0),vect.right(), 3)
print(re)
#3.
from exercise01 import *
re01=exercise01.DoubleListHelper.get_elements(list01, exercise01.Vector2(1, 0), exercise01.Vector2.right(), 3)
print(re01)


"""
# 测试．．．．．．．．．．．．．
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],]
# 10               向右　　　　　３　　　　－－> 11 12  13
re01 = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re01)

# 练习１：在二维列表中，获取23位置，向左，３个元素．
re02 = DoubleListHelper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
# 练习２：在二维列表中，获取02位置，向下，２个元素．
re02 = DoubleListHelper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
# 练习３：在二维列表中，获取20位置，右上，２个元素．
re02 = DoubleListHelper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
print(re02)
"""






