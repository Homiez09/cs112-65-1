A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

if A > 0 and B > 0:
    #find gcd
    x = A
    y = B
    while not y == 0:
        y,x = x%y, y
        tab = ""
    print(f"{tab:>2s}>> gcd({A}, {B}) = {x:>6d}")

    #find lcm 
    lcm = A*B//x
    print(f"{tab:>2s}>> lcm({A}, {B}) = {lcm:>6d}")