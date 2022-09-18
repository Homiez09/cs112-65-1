n = int(input("Enter a number: "))
m = int(input("Enter a digit: "))
count = 0
s = "s"

if n < 0:
    print("Invalid number.")
if not m // 10 == 0:
    print("Invalid digit.")
else:
    if n < 0:
        ...
    else:
        while True:
            if n % 10 == m:
                count += 1
            n //= 10
            if n == 0:
                break
        if count == 1:
            s = ""
        print(f"Digit {m} occurs {count} time{s}.")
