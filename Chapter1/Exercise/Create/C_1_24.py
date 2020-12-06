# 计算所给字符串中元音字母的个数

def count_vowel(letters):
    count={}
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    for letter in list(letters):
        if letter == 'a':
            a_count+=1
        elif letter == 'e':
            e_count+=1
        elif letter == 'i':
            i_count+=1
        elif letter == 'o':
            o_count+=1
        elif letter == 'u':
            u_count+=1
    count['a']=a_count
    count['e']=e_count
    count['i']=i_count
    count['o']=o_count
    count['u']=u_count
    return count

letters='asadfasdasdfzxcvdagsqeraf'    
print(count_vowel(letters))