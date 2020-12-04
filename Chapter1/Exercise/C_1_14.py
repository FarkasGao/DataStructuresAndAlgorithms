# 判断数组中是否存在一对乘积是奇数的互不相同的数

def count(numbers):
    number = []
    for num_1 in numbers:
        for num_2 in numbers[num_1:]:
            if num_1 == num_2:
                continue
            if (num_1*num_2)%2 ==1:
                number.append((num_1,num_2))
    return number         
               
numbers = [1,2,3,4,5,6,7,8,9]               
number = count(numbers)
print(number)