from fan.fan import Fan
from car.car import Car
from pet.pet import Pet
import pandas as pd

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
                object_holder = Fan(speed, radius, color, on)
                return [object_holder.get_speed(), object_holder.get_radius(),
                        object_holder.get_color(), object_holder.get_on()]
            except ValueError:
                print("invalid input. try again")
    elif class_choice.lower() == "car":
        while True:
            try:
                year_model: int = int(input("car year model: "))
                make: str = input("make: ")
                object_holder = Car(year_model, make)
                return [object_holder.get_year_model(), object_holder.get_make()]
            except ValueError:
                print("invalid input. try again")
    elif class_choice.lower() == "pet":
        while True:
            try:
                name: str = input("pet name: ")
                animal_type: str = input("pet animal type: ")
                age: float = float(input("pet age: "))
                object_holder = Pet(name, animal_type, age)
                return [object_holder.get_name(), object_holder.get_animal_type(),
                        object_holder.get_age()]
            except ValueError:
                print("invalid input. try again")

def name_object():
    import keyword
    while True:
        object_name = input("name this object: ")
        if object_name == '':
            print("you did not put any name")
        elif object_name[0].isnumeric():
            print("object name must not start with a number.")
        elif keyword.iskeyword(object_name):
            print("object name must not be a python reserved keyword")
        elif " " in object_name:
            print("object name must not have spaces")
        elif not object_name.isalnum():
            print("object name must not have speacial characters")
        else:
            return object_name
        
def store_object(class_name, object_name, values):
    if class_name.lower() == "fan":
        fan_values = {"speed": values[0], "radius": values[1], 
                      "color": values[2], "on": values[3]}
        fan_objects_values.append(fan_values)
        fan_objects_names.append(object_name)
    elif class_name.lower() == "car":
        car_values = {"year model": values[0], "make": values[1]}
        car_objects_values.append(car_values)
        car_objects_names.append(object_name)
    elif class_name.lower() == "pet":
        pet_values = {"name": values[0], "animal type": values[1], 
                      "age": values[2]}
        pet_objects_values.append(pet_values)
        pet_objects_names.append(object_name)

def objects_dataframe(class_name):
    if class_name.lower() == "fan":
        fan_dataframe = pd.DataFrame(fan_objects_values)
        fan_dataframe.index = fan_objects_names
        return fan_dataframe
    elif class_name.lower() == "car":
        car_dataframe = pd.DataFrame(car_objects_values)
        car_dataframe.index = car_objects_names
        return car_dataframe
    elif class_name.lower() == "pet":
        pet_dataframe = pd.DataFrame(pet_objects_values)
        pet_dataframe.index = pet_objects_names
        return pet_dataframe

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

def class_choice():
    while True:
        class_choice = input("""
    which class you want to make an object with?
    classes:
        Fan
        Car
        Pet
    ==> """)
        if class_choice.lower() == "fan":
            return "fan"
        elif class_choice.lower() == "car":
            return "car"
        elif class_choice.lower() == "pet":
            return "pet"
        else:
            print(f"no class named '{class_choice}'")

def class_runner(class_name):
    if class_name.lower() == "fan":
        return create_object("fan")
    elif class_name.lower() == "car":
        return create_object("car")
    elif class_name.lower() == "pet":
        return create_object("pet")
    else:
        print(f"no class named '{class_choice}'")

fan_objects_values = []
fan_objects_names = []

car_objects_values = []
car_objects_names = []

pet_objects_values = []
pet_objects_names = []

run = True

while run:
    menu_choice = menu()
    if menu_choice == 1:
        class_name = class_choice()
        object_name = name_object()
        object_values = class_runner(class_name)
        store_object(class_name, object_name, object_values)
        print(objects_dataframe(class_name))
    if menu_choice == 0:
        run = False