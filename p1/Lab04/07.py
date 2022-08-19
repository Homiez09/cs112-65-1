l = int(input("Enter level pokemon: "))
b = input("Enter level pokeball: ")
d = int(input("Enter distance: "))

x=0

if l > 60:
    if b == "h" or b == "H":
        x = 0.01
    elif b == "m" or b == "M":
        x = 0.08
    elif b == "l" or b == "L":
        x = 0.1
elif l > 40:
    if b == "h" or b == "H":
        x = 0.01
    elif b == "m" or b == "M":
        x = 0.05
    elif b == "l" or b == "L":
        x = 0.03
else:
    if b == "h" or b == "H":
        x = 0.01
    elif b == "m" or b == "M":
        x = 0.03
    elif b == "l" or b == "L":
        x = 0.05

s = 100 - (l * d * x)

if s < 0:
    s = 0
elif s > 100:
    s = 100

print(f"{s:.2f} percent.")