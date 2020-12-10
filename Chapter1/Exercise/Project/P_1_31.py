# 编写一个找零钱的python程序

# 最初的想法

need = float(input("所需的钱数:"))
pay = float(input("支付的钱数:"))

give_change = {'100':0,'50':0,'20':0,'10':0,'5':0,'1':0,'0.5':0,'0.1':0}

more = pay - need

def more_money(more):
    for num in num_list:
        num_float = float(num)
        if more > num_float:
            n = int(more/num_float)
            more -= num_float*n 
            give_change[num] = n
        
num_list = ['100','50','20','10','5','1','0.5','0.1']

more_money(more)
        
        
print(give_change)

# 看提示的想法(使用递归)

need = input("所需的钱数:")
pay = input("支付的钱数:")

give_change = {'100':0,'50':0,'20':0,'10':0,'5':0,'1':0,'0.5':0,'0.1':0}
num_list = ['100','50','20','10','5','1','0.5','0.1']

more = [float(pay) - float(need)]

def more_money(more, n):
    if more[0] > float(num):
        more[0] -= float(num)
        n += 1 
        n = more_money(more, n)
    return n
       

for num in num_list:
    n = 0
    n = more_money(more, 0)
    give_change[num] = n

print(give_change)