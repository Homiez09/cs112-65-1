import math
pi = math.pi
r = int(input("Enter a radius: "))
result1 = pi * (r**2)
result2 = 2 * pi * r
print(f"Area of a circle with radius {r} is {result1:.2f}")
print(f"Circumference of a circle with radius {r} is {result2:.2f}")