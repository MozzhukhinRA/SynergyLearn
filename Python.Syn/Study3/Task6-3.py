word = input()  #Надо подсчитать сколько гласных в слове
vowels = 'aeiou'
count = ''
not_count = ''
missing_vowels = ''

for i in word:
    if i in vowels:
        count += i
    else:
        not_count += i

for v in vowels:
    if v not in count:
        missing_vowels += v

print(f'Vowels:{len(count)} - {count}')
print(f'Consonants:{len(not_count)} - {not_count}')
print(f'False:{len(missing_vowels)} - {missing_vowels[:]}')