# 编写一个程序，反复从标准输入读取一行知道抛出EOFError异常（windows系统按Ctrl+Z），然后以相反的顺序输出

list1=[]
while True:
    try:
        list1.append(input())
    except EOFError:
        break
        
list1.reverse()        
for element in list1:
    print(element)