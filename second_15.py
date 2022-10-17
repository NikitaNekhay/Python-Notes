current_rus_number = 'ноль'
with open("second_15.txt", "r+", encoding='utf-8') as f:
    temp = f.read().split('\n')
    for i in temp:
        current_number = 0
        try:
            temp_lines = i.split()
            temp_line_to_translate = ' '.join(temp_lines)
            temp_temp = len(temp_lines) - 1
            current_number = int(temp_lines[temp_temp])
        except ValueError:
            print("Ошибка ввода данных в изначальный файл!")
            break
        with open("second_15_rus.txt", encoding='utf-8') as f_rus:
            temp_f_rus = f_rus.read().split('\n')
            if (len(temp_f_rus) >= current_number):
                current_rus_number = temp_f_rus[current_number - 1]
        temp_lines.remove(temp_lines[0])
        temp_lines.reverse()
        temp_lines.append(current_rus_number)
        temp_lines.reverse()
        temp.remove(temp_line_to_translate)
        temp.reverse()
        temp.append(' '.join(temp_lines))
        temp.reverse()
    temp.reverse()
    temp = "\n".join(temp)
with open("second_15_translated.txt", "w", encoding='utf-8') as f:
    f.writelines(temp)
print(f"Перевод завершён\n")
