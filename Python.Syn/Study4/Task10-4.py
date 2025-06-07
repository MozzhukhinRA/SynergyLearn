a,b = int(input()),int(input())  # Выведите все четные числа на заданном отрезке через пробел

if a <= b:
    for i in range(a,b + 1):
        if a % 2 == 0:
            print(a, end=" ")
        a += 1
else:
    print("Enter a <= b")
