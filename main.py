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
        fan_values = {"SPEED": values[0], "RADIUS": values[1], 
                      "COLOR": values[2], "ON": values[3]}
        fan_objects_values.append(fan_values)
        fan_objects_names.append(object_name)
    elif class_name.lower() == "car":
        car_values = {"YEAR-MODEL": values[0], "MAKE": values[1], "SPEED": 0}
        car_objects_values.append(car_values)
        car_objects_names.append(object_name)
    elif class_name.lower() == "pet":
        pet_values = {"NAME": values[0], "ANIMAL-TYPE": values[1], 
                      "AGE": values[2]}
        pet_objects_values.append(pet_values)
        pet_objects_names.append(object_name)

def objects_dataframe(class_name):
    if class_name.lower() == "fan":
        fan_dataframe = pd.DataFrame(fan_objects_values)
        fan_dataframe.index = fan_objects_names
        fan_dataframe.index.name = 'object'
        return fan_dataframe
    elif class_name.lower() == "car":
        car_dataframe = pd.DataFrame(car_objects_values)
        car_dataframe.index = car_objects_names
        car_dataframe.index.name = 'object'
        return car_dataframe
    elif class_name.lower() == "pet":
        pet_dataframe = pd.DataFrame(pet_objects_values)
        pet_dataframe.index = pet_objects_names
        pet_dataframe.index.name = 'object'
        return pet_dataframe

def get_object(class_name, object_name):
    if class_name.lower() == "fan":
        fan_dataframe = pd.DataFrame(fan_objects_values)
        fan_dataframe.index = fan_objects_names
        fan_dataframe.index.name = 'object'
        return fan_dataframe.loc[object_name]
    elif class_name.lower() == "car":
        car_dataframe = pd.DataFrame(car_objects_values)
        car_dataframe.index = car_objects_names
        car_dataframe.index.name = 'object'
        return car_dataframe.loc[object_name]
    elif class_name.lower() == "pet":
        pet_dataframe = pd.DataFrame(pet_objects_values)
        pet_dataframe.index = pet_objects_names
        pet_dataframe.index.name = 'object'
        return pet_dataframe.loc[object_name]
    
def modify_object(class_name, object_name):
    if class_name.lower() == "fan":
        while True:
            print("what would you like to modify in this object?")
            print(" (1) speed\n (2) radius\n (3) color\n (4) on\n (Q) Cancel")
            modify_choice = input("==> ")
            print("=" * 70)
            if modify_choice == "1":
                change_to = input("set speed to: (SLOW) (MEDIUM) (FAST) -> ")
                object_index = fan_objects_names.index(object_name)
                values = fan_objects_values[object_index]
                if change_to.lower() == 'slow':
                    values['SPEED'] = 1
                elif change_to.lower() == 'medium':
                    values['SPEED'] = 2
                elif change_to.lower() == 'fast':
                    values['SPEED'] = 3
            elif modify_choice == "2":
                change_to = input("set radius to: ")
                object_index = fan_objects_names.index(object_name)
                values = fan_objects_values[object_index]
                if change_to.isnumeric():
                    values['RADIUS'] = change_to
            elif modify_choice == "3":
                change_to = input("set color to: ")
                object_index = fan_objects_names.index(object_name)
                values = fan_objects_values[object_index]
                if change_to.isalpha():
                    values['COLOR'] = change_to
            elif modify_choice == "4":
                change_to = input("set on status to: (True) (FALSE) -> ")
                object_index = fan_objects_names.index(object_name)
                values = fan_objects_values[object_index]
                if change_to.lower == "true":
                    values['ON'] = True
                elif change_to.lower == "false":
                    values['ON'] = False
            elif modify_choice.lower() == "q":
                break
            else:
                print("Invalid input. try again")
    elif class_name.lower() == "car":
        while True:
            print("what would you like to modify in this object?")
            print(" (1) year model\n (2) make\n (3) accelerate\n (4) break\n (Q) Cancel")
            modify_choice = input("==> ")
            print("=" * 70)
            if modify_choice == "1":
                change_to = input("set year model to: ")
                object_index = car_objects_names.index(object_name)
                values = car_objects_values[object_index]
                values['YEAR-MODEL'] = change_to
            elif modify_choice == "2":
                change_to = input("set make to: ")
                object_index = car_objects_names.index(object_name)
                values = car_objects_values[object_index]
                values['MAKE'] = change_to
            elif modify_choice == "3":
                object_index = car_objects_names.index(object_name)
                values = car_objects_values[object_index]
                values['SPEED'] += 5
            elif modify_choice == "4":
                object_index = car_objects_names.index(object_name)
                values = car_objects_values[object_index]
                if values['SPEED'] != 0:
                    values['SPEED'] -= 5
            elif modify_choice.lower() == "q":
                break
            else:
                print("Invalid input. try again")
    elif class_name.lower() == "pet":
        while True:
            print("what would you like to modify in this object?")
            print(" (1) name\n (2) animal type\n (3) age\n (Q) Cancel")
            modify_choice = input("==> ")
            print("=" * 70)
            if modify_choice == "1":
                change_to = input("set name to: ")
                object_index = pet_objects_names.index(object_name)
                values = pet_objects_values[object_index]
                values['NAME'] = change_to
            elif modify_choice == "2":
                change_to = input("set animal type to: ")
                object_index = pet_objects_names.index(object_name)
                values = pet_objects_values[object_index]
                values['ANIMAL-TYPE'] = change_to
            elif modify_choice == "3":
                change_to = input("set age to: ")
                object_index = pet_objects_names.index(object_name)
                values = pet_objects_values[object_index]
                if change_to.isnumeric():
                    if not (int(change_to) < 0):
                        values['AGE'] = change_to
            elif modify_choice.lower() == "q":
                break
            else:
                print("Invalid input. try again")
    
def menu():
    print("=" * 70)
    print("Pick action: ")
    print("  (1) Create object")
    print("  (2) Display all objects")
    print("  (3) Display an object")
    print("  (4) Modify an object")
    print("  (5) Turn dataframe to csv file")
    print("  (0) Quit")
    print("-" * 70)
    menu = input("==> ")
    print("=" * 70)
    if menu.isdigit():
        return int(menu)

def class_choice():
    while True:
        print("which class you want to interact with?")
        print("classes:\n  Fan\n  Car\n  Pet")
        print("-" * 70)
        class_choice = input("==> ")
        print("=" * 70)
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

def to_csv_file(class_name, dataframe):
    if class_name.lower() == "fan":
        dataframe.to_csv('fan_objects.csv', index=True, index_label='object_name')
    elif class_name.lower() == "car":
        dataframe.to_csv('car_objects.csv', index=True, index_label='object_name')
    elif class_name.lower() == "pet":
        dataframe.to_csv('pet_objects.csv', index=True, index_label='object_name')

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
    elif menu_choice == 2:
        class_name = class_choice()
        print(objects_dataframe(class_name))
    elif menu_choice == 3:
        class_name = class_choice()
        object_name = input("name of the object: ")
        try:
            print(get_object(class_name, object_name))
        except:
            print(f"object '{object_name}' doesn't exist!")
    elif menu_choice == 4:
        class_name = class_choice()
        object_name = input("name of the object: ")
        try:
            object_values = get_object(class_name, object_name)
            modify_object(class_name, object_name)
        except:
            print(f"object '{object_name}' doesn't exist!")
    elif menu_choice == 5:
        class_name = class_choice()
        class_dataframe = objects_dataframe(class_name)
        to_csv_file(class_name, class_dataframe)
    elif menu_choice == 0:
        run = False