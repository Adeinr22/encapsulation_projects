class Car:
    def __init__(self, year_model, make):
        self.__year__model = year_model
        self.__make = make
        self.__speed = 0
    
    def __str__(self):
        return f"year model: {self.__year__model} | make: {self.__make}"
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        if self.__speed != 0:
            self.__speed -= 5
        else:
            pass
    
    def get_speed(self):
        return self.__speed
    
    def get_year_model(self):
        return self.__year__model
    
    def get_make(self):
        return self.__make
    
    def set_year_model(self, year_model):
        if str(year_model).isnumeric():
            self.__year__model = year_model
        else:
            print("invalid input")

    def set_make(self, make):
        self.__make = make