# 在不输入所有字母的情况下产生列表['a','b','c',.....]

letters = [chr(asc) for asc in range(ord('a'),ord('z')+1)]

print(letters)