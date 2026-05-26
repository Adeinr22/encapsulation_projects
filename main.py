from fan.fan import Fan
from car.car import Car
from pet.pet import Pet

def create_object(class_choice):
    if class_choice.lower() == "fan":
        while True:
            try:
                speed: str = input("pick fan speed: | (SLOW) (MEDIUM) (FAST) | -> ")
                radius: float = float(input("input the radius of the fan: "))
                color: str = input("input the color of the fan: ")
                on: str = input("turn on the fan? Yes/No | ")
                if on.lower() == "yes":
                    on: bool = True
                elif on.lower() == "no":
                    on: bool = False
                else:
                    on: bool = False
                    print("invalid input. will stay off")
                return Fan(speed, radius, color, on)
            except ValueError:
                print("invalid input. try again")
    elif class_choice.lower() == "car":
        while True:
            try:
                year_model: int = int(input("car year model: "))
                make: str = input("make: ")
                return Car(year_model, make)
            except ValueError:
                print("invalid input. try again")
    elif class_choice.lower() == "pet":
        while True:
            try:
                name: str = input("pet name: ")
                animal_type: str = input("pet animal type: ")
                age: float = float(input("pet age: "))
                return Pet(name, animal_type, age)
            except ValueError:
                print("invalid input. try again")

def menu():
    menu = input("""
    Pick action:
    (1) Create object
    (0) Quit
        
    --> """)
    if menu == "1":
        return 1
    elif menu == "0":
        return 0
    else:
        pass

def menu_choice_1():
    class_choice = input("""
    which class you want to make an object with?
      classes:
        Fan
        Car
        Pet
    ==> """)
    if class_choice.lower() == "fan":
        return create_object("fan")
    elif class_choice.lower() == "car":
        return create_object("car")
    elif class_choice.lower() == "pet":
        return create_object("pet")
    else:
        return f"no class named '{class_choice}'"
    

run = True

while run:
    menu_choice = menu()
    if menu_choice == 1:
        object = menu_choice_1()
        print(object)
    if menu_choice == 0:
        run = False