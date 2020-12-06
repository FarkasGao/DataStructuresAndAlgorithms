# 使用randint函数模拟shuffle函数

import random

def stuffle_randint(list_1):
    length = len(list_1)-1
    list_2=[]
    while list_1:
        list_2.append(list_1.pop(random.randint(0, length)))
        length-=1
    return list_2

list1 = [1,2,3,4,5]
print(stuffle_randint(list1))