my_list = list(map(int, input(). split()))

def transfer(list1, index = 0):
    if len(list1) > index:
        print(list1[index])
        transfer(list1, index + 1)
    else:
        print("The end list")

transfer(my_list)

#Напишите рекурсивную функцию, которая выведет все элементы от первого до последнего и в конце отобразит сообщение Конец списка, если выводить больше нечего