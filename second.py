city_list = []
money_list = []
with open("second.txt", "r", encoding='utf-8') as f:
    temp = f.read().split('\n')
    for i in temp:
        try:
            temp_money = i.split()
            try:
                temp_money = float(temp_money[4])
            except:
                continue
            if (temp_money < 50):
                 money_list.append(temp[temp.index(i)])
            city_res = i.index('Рим')
        except ValueError:
            continue
        city_list.append(temp[temp.index(i)])
print(f"Это информация о поездах, движущихся"
      f"в напралении Рима:\n", city_list)
print(f"Это информация о поездах, цена которых "
      f"менее 50 у.е:\n", money_list)
