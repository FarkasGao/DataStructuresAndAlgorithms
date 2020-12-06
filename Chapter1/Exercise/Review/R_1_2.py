#不使用基本运算的请况下判断是否为偶数

def is_even(k):
    for n in range(0,k+1,2):
        if n == k:
            return True
        elif n==k-1:
            return False
               
print(is_even(30))

def is_even_2(k):
    n = 0
    while n<k+2:
        if k==n:
            return True
        n+=2
    return False
    
print(is_even_2(123))

def is_even_3(k):  #比较好的选择
    l1 = list(bin(k))   #转化为二进制
    if l1[-1] == '0':
        return True
    else:
        return False
        
print(is_even_3(11))