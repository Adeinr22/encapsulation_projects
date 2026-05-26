class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        if not (age < 0):
            self.__age = age
        else:
            print("you're pet is not born yet!")

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        if not (self.__age < 0):
            return self.__age
        else:
            return 0
        
andrei_pet = Pet("Bondat", "Chicken", 1.2)
print(f"Andrei's pet name is {andrei_pet.get_name()}")
print(f"Andrei's pet animal is a {andrei_pet.get_animal_type()}")
print(f"Andrei's pet age is {andrei_pet.get_age()} years old")