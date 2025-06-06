a,b = int(input()),int(input())

if a <= b:
    for i in range(a,b + 1):
        if a % 2 == 0:
            print(a, end=" ")
        a += 1
else:
    print("Enter a <= b")