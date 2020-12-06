# 控制台输入三个整数a,b,c 并确定是否可以在正确的算数公式下成立

def count(a,b,c):
    if a*b == c:
        return True
    else:
        return False
        
print(count(int(input('a: ')), int(input('b: ')), int(input('c: '))))