# 打印"I will never spam my friend again."100次，并且应该产生8次不同随即输入错误

import random

list1 = [i for i in range(0, 100)]
sentence = "I will never spam my friend again."
sentence_list = list(sentence)
list2 = []

while True:
    if len(list2) == 8:
        break
    element = random.choice(list1)
    if element not in list2:
        list2.append(element)
for i in range(1, 101):
    if i-1 in list2:
        print(i, ': ',sentence.replace(random.choice(sentence_list), 
        random.choice(sentence_list)))
    else:
        print(i,': ',sentence)