# 编写一个索引会越界的元素列表，如果索引越界，程序捕获并打印"Don't try buffer overflow attacks in Python!"

list1 =[1,2,3,4]
try:
    print(list1[4])
except IndexError:
    print("Don't try buffer overflow attacks in Python!")