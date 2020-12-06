# 计算并返回两个数组的点积

def dot_product_list(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c
    
a=[1,1,1,1,1,0]
b=[1,2,3,4,5,6]
print(dot_product_list(a, b))