def age_convert():
    age = int(input())
    if 1 <= age <= 100:
        if age in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
            return f'{age} годa'
        elif age in (1, 21, 31, 41, 51, 61, 71, 81, 91):
            return f'{age} год'
        else:
            return f'{age} лет'
    else:
        return "A pet doesn't live that long"

print("Enter the name of the animal")

pets = {}
name_pet = {}
dict_name = input()

print("Pls, enter view your pet")
view_pet = input()
print("Pls, enter age your pet")
age_pet = age_convert()
print("Pls, enter your Name")
name_owner = input()
stats = 3

pets[dict_name] = name_pet
name_pet['Вид питомца'] = view_pet
name_pet['Возраст питомца'] = age_pet
name_pet['Имя владельца'] = name_owner

print(f'pets = {pets}')

#получить всю информацию о питомце в виде строки, как из задания по Урок №3.