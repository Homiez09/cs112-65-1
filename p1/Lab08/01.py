import math
def circle(r):
    area = math.pi * r ** 2
    return area

def circumference(r):
    area = 2 * math.pi * r
    return area

def sphere(r):
    vol = 4/3 * math.pi * r ** 3
    return vol

r = float(input("Enter a radius: "))
print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))