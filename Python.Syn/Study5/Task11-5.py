word = input()   # Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае
word1 = word[::-1]

if word == word1:
    print("Yes")
else:
    print("No")