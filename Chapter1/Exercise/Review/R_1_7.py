# 解析语法,接受并计算奇数平方和

print(sum(number**2 for number in range(int(input())+1) if (number%2==0)))