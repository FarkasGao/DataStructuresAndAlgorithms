# 模拟一个较为完善的计算器

# 这段代码待重铸

arithmetic_symbol = ['+', '-', '*', '/']

def arithmetic(int1_num, int_symbol, int3):
    try:
        int3_num = float(int3)
        if int_symbol == '+':
            print(int1_num+int3_num)
        elif int_symbol == '-':
            print(int1_num-int3_num)
        elif int_symbol == '*':
            print(int1_num*int3_num)
        elif int_symbol == '/':
            print(int1_num/int3_num)
    except ValueError:
        print("Please input a number")
        
while True:
    int1 = input()
    if int1 == 'q':
        break
    if int1 == 'c':
        continue
    try:
        int1_num = float(int1)
        while True:
            int2 = input()
            if int2 == 'q':
                break
            if int2 == 'c':
                continue
            try:
                int1_num = float(int2)
            except:
                break
        if int2 == 'q':
            break
        if int2 == 'c':
            continue
        if int2 in arithmetic_symbol:
            while True:
                int3 = input()
                if int3 == 'q':
                    break
                if int3 == 'c':
                    continue
                if int3 in arithmetic_symbol:
                    int2 = int3
                else:
                    break
            if int3 == 'q':
                break
            if int3 == 'c':
                continue
            arithmetic(int1_num, int2 ,int3)
        else:
            print("Please enter a arithmetic symbol")
        
    except ValueError:
        print("Please input any number first")