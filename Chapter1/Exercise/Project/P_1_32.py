

arithmetic_symbol = ['+', '-', '*', '/']

def arithmetic(int1_num, int_symbol, int3):
    try:
        int3_num = int(int3)
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
    try:
        int1_num = int(int1)
        int2 = input()
        if int2 == 'q':
            break
        if int2 in arithmetic_symbol:
            int3 = input()
            if int3 == 'q':
                break
            arithmetic(int1_num, int2 ,int3)
        else:
            print("Please enter a arithmetic symbol")
        
    except ValueError:
        print("Please input any number first")
        continue