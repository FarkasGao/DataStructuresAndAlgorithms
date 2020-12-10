# 验证生日悖论

import random

birthday_dictionary = {}
for n in range(5, 101, 5):
    same_birthday = 0
    for i in range(100):
        list_birthday = []
        for i in range(n):
            birthday = random.randint(1, 365)
            if birthday in list_birthday:
                same_birthday += 1
                break
            list_birthday.append(birthday)
    birthday_dictionary[str(n)] = same_birthday/100
    
print(birthday_dictionary)