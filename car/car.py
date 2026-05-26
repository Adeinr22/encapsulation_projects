class Car:
    def __init__(self, year_model, make):
        self.__year__model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        if self.__speed != 0:
            self.__speed -= 5
        else:
            pass
    
    def get_speed(self):
        return self.__speed
        
wigo = Car(2020, "Toyota")
for acc in range(5):
    wigo.accelerate()
    print(wigo.get_speed())
for brk in range(5):
    wigo.brake()
    print(wigo.get_speed())