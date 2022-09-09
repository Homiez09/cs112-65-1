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
    if n >= 1 and n <= 999:
        number.append(n)
    else:
        print("Number is out of range.")
        
print(f"Original list:\n{number}")
print("Accumulative Sum:")
accum_sum(number)
