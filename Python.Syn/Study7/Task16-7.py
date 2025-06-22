num1 = int(input())
num2 = list(map(int,input().split()))
num3 = set()
num4 = set()

num2.sort()

num2 = [wal for wal in num2 if wal <= 2000000000]

if 1 <= num1 <= 100000:
    if num1 == len(num2):
        for i in num2:
            if i in num3:
                num3.discard(i)
                num4.add(i)
            else:
                num3.add(i)
        for i in num4:
            if i in num3:
                num3.discard(i)
        print(f'Various numbers: {len(num3)} ----- (it {num3})')
    else:
        print(f'Quantitatively {len(num2)} should be equal {num1}')

#Выведите число, равное количеству различных чисел среди данных.