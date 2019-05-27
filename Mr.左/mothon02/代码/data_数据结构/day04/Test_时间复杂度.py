# 时间复杂度
# 　运算此时为　n
# 　时间复杂度 　O(n)
def fun(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

# 运算次数　　3次
# 时间复杂度　O(1)
def fun01(n):
    sum = (1 + n) * n / 2
    return sum

# 运算次数　n^2+n
# 时间复杂度
# l[[1,2,3],[4,5,6],[7,8,9]]
def fun02(l):
    for i in l:
        for j in i:
            print(j, end=' ')
        print()

print("fun:", fun(100))
print("fun01:", fun(100))
print("fun02:", fun(100))
