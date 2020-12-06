def minmax(data):       #获取最大最小值
    min_num = data[0]
    max_num = data[0]
    for i in range(len(data)):
        if min_num > data[i]:
            min_num = data[i]
        if max_num < data[i]:
            max_num = data[i]
            
    return min_num,max_num
    
numbers = [1,2,3,4,9,8,7,6,5]    
print(minmax(numbers))