# 返回一个删除了所有标点符号的字符串

def delete_mark(s):
    s_list = list(s)
    for element in s_list:
        if ord(element)!=32:
            if ord(element)<65 or 90<ord(element)<97 or ord(element)>122:
                s_list.remove(element)
    s=''
    for element in s_list:
        s += element
    return s
    
s = "Let's try, Mike."    
print(delete_mark(s))