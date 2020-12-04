# 编写一个函数的伪代码描述，用来逆置列表

#def reverse_逆置列表(列表 )

#n = len(列表)
#if n%2 == 0
#for i in range(0,n/2+1)
#列表[i],列表[n-i] = 列表[n-i],列表[i]

def reverse_1(l1):
    n=len(l1)
    for i in range(0,int(n/2)):
        l1[i],l1[-i-1] = l1[-i-1],l1[i]
        print(l1)

li = [1,2,3,4,5,6,7,8]    
reverse_1(li)