class Fan:
    SLOW, MEDIUM, FAST = 1, 2, 3
    def __init__(self, speed, radius, color):
        __speed: int = speed
        __on: bool = False
        __radius: float = radius
        __color: str = color
