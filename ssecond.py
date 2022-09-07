s = input("Enter the line: ")
flag = 0

max_symb = s[0]
max = 0
temp = 0
i = 0
ii = 0

while i < len(s):
    ii = i
    temp = 0
    while ii < len(s):
        if s[i] == s[ii]:
            temp += 1
        ii += 1
    if temp > max:
        max = temp
        max_symb = s[i]
    i += 1

print("символ, который появляется наиболее часто -", max_symb, "; встречается в таком количестве - ", max)
