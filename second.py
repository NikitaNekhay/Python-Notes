import random

# greeting = "Hallo, "
# input_name="Input your name: "
# name = input(input_name)
# print(greeting+name)
# print(3*name)

# greeting = "Hallo, "
# print("Straight_symbold -", greeting[0], greeting[5] ,greeting[6],greeting[-6])
# print("Reverse 1 -", greeting[-2:-7])
# print("Reverse 2 -", greeting[-7:-2])


numb_r = (input("Наше число - "))
len_s = len(numb_r)
# numb_r = int(numb_r)
i = 0
sum_r = 0
while i < len_s:
    sum_r += int(numb_r[i])
    i += 1
print("Сумма цифр - ", sum_r)

# # Форматирование строк (lower, upper...)
# l = "hnaah fekol"
# u= "SFFS SSS"
#
# #Tittle Первая буква всех слов в заглавн
# print(l.title())
#
# #Capitalize первая буква в заглавн. а все остальные в нижний
# print(l.capitalize())
#
# #
# print(l.upper())
#
# #
# print(l.lower())
#
# # верхний рег. превр. в нижн. рег.
# print(l.swapcase())
#
# # True - если все слова строки в нижнем регистре False - наооборот
# print(l.isupper())
# print(u.isupper())
#
#line = 'ааа,bbb,ссссс,dd\n'
#line.rstrip()          #Удалить пробельные символы с правой стороны
#                       #'ааа,bbb,ссссс,dd'
#line.rstrip().split(',')            #Скомбинировать две операции
#                       #('ааа', 'bbb', 'ссссс', 'dd')
# С
#
#

s = input("Input the line: ")
symb = input("Input the symbol to avoid in the line: ")
flag = 0
ch_symb = "&"
# s = "Herroies wiere reborin at this place i"

for i in s:
    if s.find(symb) != -1:
        # s[i] = ch_symb
        flag = 1
if flag == 1:
    s = s.split(symb)
    s = ''.join(s)
    print("Строка была изменена: ", s)
else:
    print("Такого символа не было найдено")
