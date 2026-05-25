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

fan = Fan()
print(fan)