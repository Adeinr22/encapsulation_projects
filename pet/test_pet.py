from pet import Pet

andrei_pet = Pet("Bondat", "Chicken", 1.2)
print(f"Andrei's pet name is {andrei_pet.get_name()}")
print(f"Andrei's pet animal is a {andrei_pet.get_animal_type()}")
print(f"Andrei's pet age is {andrei_pet.get_age()} years old")