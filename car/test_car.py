from car import Car

wigo = Car(2020, "Toyota")
for acc in range(5):
    wigo.accelerate()
    print(f"the car accelerates! the speed is now: {wigo.get_speed()}")
for brk in range(5):
    wigo.brake()
    print(f"the car breaks! the speed is now: {wigo.get_speed()}")