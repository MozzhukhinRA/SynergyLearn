pets = {}
name_pets = {}
new_pets = {}
print("Select: create, read, update or del entry depending on what you want to do")


def age_convert():
    age = int(input("Pls, enter age your pet: "))
    if 1 <= age <= 100:
        if age in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
            return f'{age} годa'
        elif age in (1, 21, 31, 41, 51, 61, 71, 81, 91):
            return f'{age} год'
        else:
            return f'{age} лет'
    else:
        return "A pet doesn't live that long"


def create():
    pets_count = max(pets.keys(), default=0) + 1
    while True:
        dict_name = input("Enter the name of the animal: ")
        view_pet = input("Pls, enter view your pet: ")
        age_pet = age_convert()
        name_owner = input("Pls, enter your Name: ")

        name_pet = {
            "Вид питомца":view_pet,
            "Возраст питомца":age_pet,
            "Имя владельца":name_owner
        }

        pets[pets_count] = {dict_name: name_pet}
        pets_count += 1
        print(pets)

        while True:
            command = input("Do you wont continue? (yes or no): ")
            if command == "yes":
                break
            elif command == "no":
                print("Select: create, read, update or del entry depending on what you want to do")
                return
            else:
                print("Not Found")


def read():
    while True:
        unit1 = int(input("Enter number of pet: "))
        while True:
            if unit1 in pets:
                print(pets[unit1])
                print('\n',"Select: create, read, update or del entry depending on what you want to do")
                return
            else:
                print("Not Found")
                break


def delete():
    while True:
        unit1 = int(input("Enter number of pet: "))
        while True:
            global pets
            if unit1 in pets:
                pets.pop(unit1)
                pets = {i+1: v for i, v in enumerate(pets.values())}
                print(pets)
                return
            else:
                print("Not Found")
                break


def update():
    while True:
        unit1 = int(input("Enter number on pets in list: "))
        while True:
            global name_pets
            global new_pets
            if unit1 in pets:
                dict_name = input("Enter the name of the animal: ")
                unit2 = input("Pls, enter view your pet: ")
                unit3 = age_convert()
                unit4 = input("Pls, enter your Name: ")
                new_pets = {
                    "Вид питомца": unit2,
                    "Возраст питомца": unit3,
                    "Имя владельца": unit4
                }
                pets[unit1] = {dict_name: new_pets}
                print("Update completed")
                return
            else:
                print("Not Found")
                break


while True:
    action = input()
    if action == "create":
        create()
    elif action == "read":
        read()
    elif action == "del":
        delete()
    elif action == "update":
        update()
    elif action == "stop":
        break
    else:
        print("Not Found command")

#База ветклиники
