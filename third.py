list = [13, 56, 'Python', 34, 19, 'love']
flag = 0
ii = 0
jj=0
sum = 0
temp = 0
for i in list:
    if isinstance(i, int):
        flag = 1
        if i % 2 == 0:
            sum = 0
            for j in str(i):
                sum += int(j)
            print(f"{i} - четное число и сумма цифр в нём равна: ", sum)
        else:
            temp = ii
            list.remove(i)
            list.insert(temp, 1)
    ii += 1
print(list)