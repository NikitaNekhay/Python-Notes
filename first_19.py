import os
counter_lines_f = 0
end_of_line = "\n"
numbers = "0123456789"
flag_number = 0
list_to_f2 = []
with open("first_2_19.txt", "w", encoding='utf-8') as f2:
    with open("first_1_19.txt", "w", encoding='utf-8') as f1:
        print(f"Введите строки, которые будут записаны в файл."
              "Для того, чтобы прекратить запись введите пустую строку")
        var = '1'
        while (var != ''):
            var = input()
            f1.write(var+end_of_line)
            counter_lines_f += 1
            if(counter_lines_f % 2 != 0):
                list_to_f2.append(var+end_of_line)
    f2.writelines(list_to_f2)
f1_name=r"Y:\Projects\Python\UNI\СЯП\ЛАБА3\first_1_19.txt"
f2_name=r"Y:\Projects\Python\UNI\СЯП\ЛАБА3\first_2_19.txt"
f1_stats = os.stat(f1_name)
f2_stats = os.stat(f2_name)
print(f"Количество байт в первом файле - {f1_stats.st_size}")
print(f"Количество байт во втором файле - {f2_stats.st_size}")
