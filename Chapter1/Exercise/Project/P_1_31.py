need = float(input("所需的钱数:"))
pay = float(input("支付的钱数:"))

give_change = {'100':0,'50':0,'20':0,'10':0,'5':0,'1':0,'0.5':0,'0.1':0}

more = pay - need

def more_money(num, more):
    num_float = float(num)
    if more > num_float:
        n = int(more/num_float)
        give_change[num] = n
        return n*num_float
    return 0
    
num_list = ['100','50','20','10','5','1','0.5','0.1']

for num in num_list:
        more -= more_money(num, more)
    
    
print(give_change)