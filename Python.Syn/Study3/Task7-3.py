minInv = int(input())   #Задача про двух инветсоров в которой мы считаем кто может вложиться в стартап
Mike = int(input())
Ivan = int(input())
if Mike >= minInv and Ivan >= minInv:
    print(2)
elif Mike >= minInv and Ivan == 0:
    print("Mike")
elif Mike == 0 and Ivan >= minInv:
    print("Ivan")
elif Mike < minInv and Ivan < minInv:
    if Mike + Ivan >= minInv:
        print(1)
    else:
        print(0)