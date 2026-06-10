from fan import Fan

# object creation
fan_1 = Fan()
fan_2 = Fan()

# fan_1 assignment of values
fan_1.set_speed(Fan.FAST)
fan_1.set_radius(10)
fan_1.set_color("yellow")
fan_1.set_on(True)

# fan_2 assignment of values
fan_2.set_speed(Fan.MEDIUM)
fan_2.set_radius(5)
fan_2.set_color("blue")
fan_2.set_on(False)

# fan_1 displaying values
print(fan_1.get_speed())
print(fan_1.get_radius())
print(fan_1.get_color())
print(fan_1.get_on())
print("-"*100)

# fan_2 displaying values
print(fan_2.get_speed())
print(fan_2.get_radius())
print(fan_2.get_color())
print(fan_2.get_on())
print("-"*100)

# Comparison
print(f"""
{"="*100}
fan no.1: {fan_1}
{"-"*100}
fan no.2: {fan_2}
{"="*100}
""")
