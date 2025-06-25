import math

list_my = []

def conv_fact():
    num = int(input())
    num = math.factorial(num)
    for i in range(num):
        i += 1
        i = math.factorial(i)
        list_my.append(i)
    list_my.reverse()

conv_fact()
print(list_my)

#В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3)
# и вам нужно сделать список из факториалов числа 6 в убывающем порядке.
# Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1