# 接受并计算奇数平方和

def odd_square_sum(n):
    sum_num = 0
    for i in range(n+1):
        if i%2==0:
           sum_num += i**2 
    print(sum_num)
    
odd_square_sum(3)