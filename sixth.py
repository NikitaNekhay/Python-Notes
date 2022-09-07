# my_cort = input("Введите через запятую кортеж: ")
# print(type(my_cort))

my_cort = tuple((421, 42, 21, 24, 512, 2, 4, 221, 35, 6, 8, 89, 3, 57, 9))
sum_cort = 0

for i in my_cort:
    if i % 2 == 0:
        sum_cort+=i
print(f"{my_cort} - это наш кортёж")
print(f"Сумма чётных элементов кортежа - {sum_cort}")