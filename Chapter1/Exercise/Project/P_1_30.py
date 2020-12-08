# 输入一个大于2的整数，反复用2整除，知道商数小于2

num = int(input())

i = 1
while num >= 2**i:
    i += 1
    
print(i-1)

# 提示的方法1  递归

num = int(input())
index = 0
def divide(num, index):
    if num>=2:
        num = num/2
        index += 1 
        index = divide(num, index)
    return index
    
index = divide(num, index)
print(index)

# 提示的方法2  log()函数

import math
print(int(math.log(int(input()),2)))