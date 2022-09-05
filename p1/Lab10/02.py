number = []

def accum_sum(l):
    total = 0
    for i in l:
        total += i 
        print(total)

while True:
    n = int(input("Enter a number (0 to end): "))
    if n == 0:
        break
    elif n < 1 or n > 999:
        print("Number is out of range.")
        n = int(input("Enter a number (0 to end): "))
    number.append(n)
print(f"Original list:\n{number}")
print("Accumulative Sum:")
accum_sum(number)
