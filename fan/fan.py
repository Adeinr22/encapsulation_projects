class Fan:
    SLOW, MEDIUM, FAST = 1, 2, 3
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed: int = speed
        self.__radius: float = radius
        self.__color: str = color
        self.__on: bool = on  
    
    def __str__(self):
        return f"speed: {self.__speed} \
                 radius: {self.__radius} \
                 color: {self.__color} \
                 on: {self.__on}"
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        if speed == 1 or 2 or 3:
            self.__speed: int = speed
        else:
            print("Invalid input: options are 1, 2, or 3")
            
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if 0 < radius:
            self.__radius = radius
        elif radius < 0:
            print("Invalid Input: Fan's radius can't be negative")
        else:
            print("Invalid Input: must be a number")
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        if str(color).isalpha():
            self.__color = color
        else:
            print("Invalid input: must be a color")

    def get_on(self):
        return self.__on
    
    def set_on(self, status):
        if status == True or status == False:
            self.__on = status
        elif str(status).lower() == "true":
            self.__on = True
        elif str(status).lower() == "false":
            self.__on = False
        else:
            print("Invalid input: must only be True or False")