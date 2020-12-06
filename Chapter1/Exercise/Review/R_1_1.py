#判断一个数是否为另一个数的因数

def is_multiple(n, m):
    return True if n%m==0 else False
    
print(is_multiple(5, 2))