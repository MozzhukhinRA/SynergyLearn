string_num = int(input())    #Переверните массив чисел. Выведите N чисел - перевернутый массив
numb = []
for i in range(string_num):
    num = abs(int(input()))
    if 1 <= num <= 10000:
        numb.append(num)
    else:
        break
numb.reverse()
print(numb)