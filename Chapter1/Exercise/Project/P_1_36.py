# 输出列表中每个单词出现的次数

sentence = 'This is a sentence'
sentence = sentence.lower()
word = list(sentence)
word_set = set(word)
letter_dic = {}
for letter in word_set:
    count = 0
    while True:
        if letter in word:
            word.remove(letter)
            count += 1
        else:
            break
    letter_dic[letter] = count

del letter_dic[' ']
    
print(letter_dic)