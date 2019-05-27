list01=["a","b","c"]
list02=[101,102,103]
list03=["张三丰","张无忌","赵敏"]
# for item in enumerate(list):
#     print(item)
#
# for index,element in enumerate(list):
#     print(index,element)

def my_enumerate(target):
    index=0
    for item in target:
        yield index,item
        index+=1

for item in my_enumerate(list01):
    print(item)

# ---------zip-------------
def my_zip(target01,target02):
    for index in range(len(target01)):
        yield target01[index],target02[index]

for item in my_zip(list02,list03):
    print(item)











