# 用解析语法生成列表[1,2,4,8,16,32,64,128,256]

numbers=[]
for square in range(0,9):
    numbers.append(2**square)
    
print(numbers)