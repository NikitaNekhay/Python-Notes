counter_lines_f = 0
end_of_line = "\n"
numbers = "0123456789"
flag_number = 0

with open("first_1_12.txt", "w", encoding='utf-8') as f1:
    print(f"Введите строки, которые будут записаны в файл."
          "Для того, чтобы прекратить запись введите пустую строку")
    var = '1'
    while (var != ''):
        var = input()
        f1.write(var+end_of_line)
        counter_lines_f += 1
        flag_skip_space = 0

with open("first_2_12.txt", "w", encoding='utf-8') as f2:
    list_to_f2 = []
    list_of_lines_with_numbers = []
    with open("first_1_12.txt", encoding='utf-8') as f1:
        temp_f1 = f1.read()
        f1_lines = temp_f1.split("\n")
        for i in f1_lines:
            f1_lines_words = i.split()
            flag_number = 0
            for j in f1_lines_words:
                for m in j:
                    if m in numbers:
                        flag_number = 1
            if flag_number == 1:
                list_of_lines_with_numbers.append(i + end_of_line)
            else:
                list_to_f2.append(i + end_of_line)
    f2.writelines(list_to_f2)
with open("first_2_12.txt", encoding='utf-8') as f2:
    temp = f2.read()
    temp_lines = temp.split('\n')
    temp_last_line = temp_lines[len(temp_lines) - 4]
    list_of_last_line = temp_last_line.split()
    print(f"Количество слов в последней строке второго файла - {len(list_of_last_line)}")
