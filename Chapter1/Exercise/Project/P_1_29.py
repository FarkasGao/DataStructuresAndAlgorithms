#返回'c','a','t','d','o','g'所有可能的组合

storage = ['','','','','','']
storage[0]=['c','a','t','d','o','g']
combination=[]

for initial in storage[0]:
    storage[1]=storage[0][:]
    storage[1].remove(initial)
    for second in storage[1]:
        storage[2]=storage[1][:]
        storage[2].remove(second)
        for third in storage[2]:
            storage[3]=storage[2][:]
            storage[3].remove(third)
            for forth in storage[3]:
                storage[4]=storage[3][:]
                storage[4].remove(forth)
                for fifth in storage[4]:
                    storage[5]=storage[4][:]
                    storage[5].remove(fifth)
                    combination.append(initial+second+third+forth+fifth+storage[5][0])
                                        
print(combination)
print(len(combination))


#看提示后的尝试

combination = []

def recursion(letters,element):
    if not letters:
        combination.append(element)
        
    for letter in letters:
        letters_list = letters[:]
        letters_list.remove(letter)
        element = element + letter
        recursion(letters_list,element)
        element = element.strip(letter)
        
letters = ['c','a','t','d','o','g']
element=''
recursion(letters, element)
print(combination)
print(len(combination))


#网上档的代码

def perm(s=''):
    #这里是递归函数的出口，为什么呢，因为这里表示：一个长度为1的字符串，它的排列组合就是它自己。
    if len(s)<=1:
        return [s]
    sl=[] #保存字符串的所有可能排列组合
    for i in range(len(s)):  #这个循环，对应 解题思路1）确定字符串的第一个字母是谁，有n种可能（n为字符串s的长度
        for j in perm(s[0:i]+s[i+1:]): #这个循环，对应 解题思路2）进入递归，s[0:i]+s[i+1:]的意思就是把s中的s[i]给去掉
            sl.append(s[i]+j) # 对应 解题思路2）问题就从“返回字符串中的字母排列组合” **变成了** “返回 第一个字母+除去第一个字母外的字符串的排列组合”
    return sl
 
def main():
    perm_nums=perm('catdog') # 有可能存在字母相同的情况
    no_repeat_nums = list(set(perm_nums)) # 去重，挺牛的，这个代码
    print('perm_nums', len(perm_nums), perm_nums)
    print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
    pass
 
if __name__ == '__main__':
    main()
    