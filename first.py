f2 = open("first_2.txt", "w")
f2.close()
f2 = open("first_2.txt", "a")

with open("first_1.txt", "w") as f1:
    1
with open("first_1.txt", "a") as f1:
    print(f"Введите строки, которые будут записаны в файл."
          "Для того, чтобы прекратить запись введите пустую строку")
    empty_s = "\n"
    s = "s"
    list_to_file = []
    while (s != "\n"):
        s = str(input(f"Ваша строка: "))
        s = s + empty_s
        list_to_file.append(s)  # f1.write(s)
    f1.writelines(list_to_file)
    list_to_file.clear()
with open("first_1.txt") as f1:
    flag1 = 0
    for a in f1:
        temp = a.split()
        count = 0
        for i in temp:
            count += 1
        if (count == 1):
            i = i + s
            list_to_file.append(i)
            flag1 = 1  # вызвать ф-ию добавления этой строки в f2
    f2.writelines(list_to_file)
    list_to_file.clear()
f2.close()

if (flag1 != 0):
    with open("first_2.txt", "r") as f2:
        obj_max = -1
        content = f2.read()
        content = content.split("\n")
        min = len(content[0])
        for i in content:
            counter = len(i)
            if (counter < min and i != ''):
                min = counter
                obj_max = i
    print(f"\n\nЭто строка, являющася одним лишь словом является"
            f" самой короткой из строк такого же типа: ", obj_max)
else:
    print(f"\n\nНе было найдено ни одного слова")
