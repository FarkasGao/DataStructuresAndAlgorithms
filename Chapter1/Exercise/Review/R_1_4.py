def squares_sum(n):   #计算平方和
    sum=0
    for i in range(n+1):
        sum += i**2
        
    return sum
    
print(squares_sum(10))