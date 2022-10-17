end_of_line = '\n'
counter_lines_f = 0
flag_k = 0
flag_vowel = 0
vowels_rus = "аеёуяиюэоыАЕЁУЯИЮЭОЫ"
vowels_eng = "aeiouyAEIOUY"

with open("first_1_3.txt", "w", encoding='utf-8') as f1:
    print(f"Введите строки, которые будут записаны в файл."
          "Для того, чтобы прекратить запись введите пустую строку")
    var = '1'
    while (var != ''):
        var = input()
        f1.write(var + end_of_line)
        counter_lines_f += 1
while (flag_k != 1):
    try:
        k = int(input("Введите номер строки, начиная с которой она и последующие 5шт. будут записаны в другой файл:"))
    except:
        print("Неверный тип данных!\n")
        continue
    if (k > counter_lines_f or k < 0):
        print("Значение k должно быть не больше количества введенных вами строк и не меньше нуля. Попробуйте ещё раз\n")
        if (counter_lines_f == 0):
            print("Вы ввели только пустую строку.\n")
        continue
    else:
        flag_k = 1
with open("first_2_3.txt", "w", encoding='utf-8') as f2:
    list_to_f2 = []
    with open("first_1_3.txt", encoding='utf-8') as f1:
        temp_f1 = f1.read()
        f1_lines = temp_f1.split('\n')
        max = 0
        temp_for_max = f1_lines[0].split()
        max_ind = temp_for_max[0]
        for i in f1_lines:
            f1_lines_words = i.split()
            count_vowel = 0
            for j in f1_lines_words:
                for m in j:
                    if m in vowels_eng or m in vowels_rus:
                        count_vowel += 1
                        flag_vowel = 1
            if (max < count_vowel):
                max = count_vowel
                max_ind = i
            count_write = 0
        for i in f1_lines:
            if i is not f1_lines[k - 1] and count_write == 0:
                continue
            if count_write == 5:
                break
            if i is not max_ind:
                list_to_f2.append(i + end_of_line)
            count_write += 1
    f2.writelines(list_to_f2)
with open("first_2_3.txt", encoding='utf-8') as f2:
    temp = f2.read()
    count_vowel = 0
    for i in temp:
        if i in vowels_eng or i in vowels_rus:
            count_vowel += 1
print(f"Количество  гласных букв во втором файле - {count_vowel}")
