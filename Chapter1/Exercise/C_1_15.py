# 判断一个数字序列所有数是否是不同的

def set_number(numbers):
    numbers_2 = set(numbers)
    if len(numbers) != len(numbers_2):
        return False
    else:
        return True
        
numbers=[1,4,6,7,3,5]
print(set_number(numbers))