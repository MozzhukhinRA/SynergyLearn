print("Enter S - if area and P - if perimetr")
variant = input()

if variant == "S" or variant == "s":
    print("Enter side rectangle")
    a, b = map(float, input().split())
    s = a*b
    print(s)
elif variant == "P" or variant == "p":
     print("Enter side rectangle")
     a, b = map(float, input().split())
     p = 2*(a+b)
     print(p)
else:
    print("Pls, try again")