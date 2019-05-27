list = [2,3,4,6]
list01=[]
# for item in list:
#     if item >= 3:
#         result=item
#         list01.append(result)
# print(list01)

result01=[ item for item in list if item >= 3 ]
print(result01)

result02=(item for item in list if item >= 3 )
print(result02)






















