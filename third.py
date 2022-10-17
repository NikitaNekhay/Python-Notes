dict_discipline = {}
with open("third_1.txt", encoding='utf-8') as f:
    temp_file = f.read()
    temp_file_lines = temp_file.split('\n')
    temp_name = 'Hi'
    i = 0
    while (temp_file_lines[i] != ''):
        temp_name = temp_file_lines[i].split(":")
        temp_hours = temp_name[1].split()
        sum = 0
        for k in temp_hours:
            temp_one_hour = k.split('(')
            try:
                sum += int(temp_one_hour[0])
            except:
                continue
        dict_discipline.update({temp_name[0]: sum, })
        i += 1
print(dict_discipline.items())
