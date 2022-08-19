m = int(input("Minutes before due: "))
t = float(input("Temperature: "))
r = input("Is it raining (y/n)? ")

day = m/1440

if day - int(day) >= 0.5:
    day = int(day) + 1
else:
    day = int(day)

print(f">>> {day} days before due.")

if day < 2:
    print(">>> I will do the assignment.")
elif day > 5:
    print(">>> I will not do the assignment.")
elif t > 40 or t > 25 and (r == "y" or r == "Y"):
    print(">>> I will not do the assignment.")
else: 
    print(">>> I will do the assignment.")