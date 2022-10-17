end_of_line = '\n'
counter_lines_f = 0
flag_k = 0
flag_feature = 0
feature = "А"
count_feature = 0
max_feature = 0
count_similar_words = 0
max_A = 'Не было найдено слова с буквой А'

with open("first_1_14.txt", "w", encoding='utf-8') as f1:
    print(f"Введите строки, которые будут записаны в файл."
          "Для того, чтобы прекратить запись введите пустую строку")
    var = '1'
    while (var != ''):
        var = input()
        f1.write(var + end_of_line)
        counter_lines_f += 1

with open("first_2_14.txt", "w", encoding='utf-8') as f2:
    list_to_f2 = []
    with open("first_1_14.txt", encoding='utf-8') as f1:
        temp_f1 = f1.read()
        f1_lines = temp_f1.split('\n')
        f1_lines = ' '.join(f1_lines)
        f1_lines = f1_lines.split()
        for i in f1_lines:
            f1_lines_words = i.split()
            count_feature = 0
            for j in i:
                if j in feature:
                    count_feature += 1
                    flag_feature = 1
            if (max_feature < count_feature):
                max_feature = count_feature
                max_A = i
        if max_A !='Не было найдено слова с буквой А':
            print(f"Слово, в котором наибольшее количество включений буквы А - {max_A} {f1_lines.index(max_A)+1}")
        else:
            print(f"Слово, в котором наибольшее количество включений буквы А - {max_A} {None}")
        f1_lines = temp_f1.split('\n')
        for i in f1_lines:
            list_words = i.split()
            #count_similar_words = 0 # было здесь
            if (len(list_words) >= 2):
                for ii in list_words:
                    count_similar_words = 0
                    kk = ii
                    for kk in list_words:
                        if kk == ii:
                            count_similar_words += 1
                    if (count_similar_words == 2):
                        list_to_f2.append(i + end_of_line)
                        break
            else:
                continue
    f2.writelines(list_to_f2)
