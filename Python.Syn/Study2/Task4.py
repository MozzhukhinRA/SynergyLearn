print("Pls enter only five-digit number")
z = list(map(float,input()))
unit = (z[-2] ** z[-1]) * z[-3] / (z[0] - z[1])
print(unit)