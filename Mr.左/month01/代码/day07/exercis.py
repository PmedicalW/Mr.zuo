# # 自定义列表的排序函数
# # 　　温馨提示：返回值需要吗？
def get_min(list):
    for l in range(len(list) - 1):
        for i in range(l + 1, len(list)):
            if list[l] > list[i]:  # 两两元素比较
                list[l], list[i] = list[i], list[l]  # 两两交换


list01=[1,9,1,2,7,3,5]
get_min(list01)
print(list01)






