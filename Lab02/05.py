import math
distance = int(input())
fuelMax = int(input())
keaw = fuelMax - (fuelMax * (51/100))
kwan = fuelMax - (fuelMax * (11/100))   
x = distance/(keaw*15)
y = distance/(kwan*15)
print(math.ceil(x))
print(math.ceil(y))