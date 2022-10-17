import json

vage = 0
average_vage = 0
average_number = 0
dict_firms = {}
dict_unprofit_firms = {}
flag_av = 0
flag_unprofit = 0

with open("fourth.txt", encoding='utf-8') as f:
    temp = f.read()
    temp_lines = temp.split('\n')
    for i in temp_lines:
        temp_words = i.split()
        len_list = len(temp_words)
        if(len_list == 4):
            try:
                vage = int(temp_words[len_list - 2]) - int(temp_words[len_list - 1])
            except IndexError:
                continue
            dict_firms.update({temp_words[0]: vage})
            if (vage >= 0):
                average_vage += vage
                average_number += 1
            else:
                dict_unprofit_firms.update({temp_words[0]: vage})
                flag_unprofit = 1
        else:
            continue
if temp == '':
    print("Файл с информацией о фирмах пустой\n")
else:
    if average_number == 0:
        if flag_unprofit == 1:
            print("Все фирмы потерпели убытки!\n")
    else:
        dict_firms_average = {'average vage': average_vage / average_number}
        flag_av = 1
    with open("fourth.json", "w", encoding='utf-8') as f_json:
        json.dump(dict_firms, f_json)
        if (flag_av == 1):
            json.dump(dict_firms_average, f_json)
