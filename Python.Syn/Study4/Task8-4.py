N = int(input()) #в этой задаче мы вводим N целых чисел и считаем сколько из них равно нулю
count = 0

for i in range(N):
    z = int(input())
    if z == 0:
        count += 1
print(count)