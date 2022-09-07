my_dict = {'a': 50, 'b': 5, 'c': 56, 'd': 4, 'e': 58, 'f': 20}
copy_my_dict = my_dict.copy()

flag = 0
flag1 = 0
while flag != 3:
    for i in my_dict:
        if flag1 == 0:
            temp = my_dict.setdefault(i)
            key_min = i
            flag1 = 1
        if my_dict.setdefault(i) < temp:
            temp = my_dict.setdefault(i)
            key_min = i
    flag1 = 0
    flag += 1
    print(f"{flag} минимальный элемент - это ", temp)
    my_dict.pop(key_min)

