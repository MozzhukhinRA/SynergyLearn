num1 = set(input().split())
num2 = set(input().split())
num3 = set()

for i in num1:
    if i in num2:
        num3.add(i)

print(f'Simultaneous numbers in the list: {len(num3)}')
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором
