z = int(input())  #Задача на вход которой подается число а на выходе получаем его текстовое описание

if z > 0 and z % 2 == 0:
    print("Positive even number")

elif z > 0 and z % 2 == 1:
    print("Positive NOT even number")

elif z < 0 and z % 2 == 0:
    print("Negative even number")

elif z < 0 and z % 2 == 1:
    print("Negative NOT even number")

else:
    print("Zero number")