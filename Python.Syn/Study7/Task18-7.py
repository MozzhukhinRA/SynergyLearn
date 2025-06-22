num1 = list(map(int,input().split()))
num2 = set()
num3 = set()

for i in num1:
    if i in num2:
        num2.discard(i)
        num3.add(i)
    else:
        num2.add(i)

for i in num3:
    print(f'{i}')
    print("YES")

for i in num2:
    print(f'{i}')
    print("NO")
