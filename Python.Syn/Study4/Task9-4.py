num = int(input())    #В задаче вывожу все натуральные числа введенного числа

for i in range(num):
    i += 1
    if num % i == 0:
        print(i)
