# 二分法查找
def search(l, key):
    low = 0
    hight = len(l) - 1
    while low <= hight:
        mid = (low + hight) // 2
        if l[mid] < key:
            low = mid + 1
        elif l[mid] > key:
            hight = mid - 1
        else:
            return mid
    return

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 数据需是排好序的
print(search(l, 6))
