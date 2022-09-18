n = int(input("Enter a number: ")) + 1
i = 0
j = 0
if n < 1:
    print("Invalid input, program terminates.")
else:
    while i < n:
        if i < 2:
            print(f"{i}! = 1 = 1")
        else:
            text = f"{i}! = "
            result = 1
            while j < i:
                text += str(i-j)
                result *= i-j
                if j < i-1:
                    text += " x "
                else:
                    text += " = "
                j+=1
            j = 0
            print(text + f"{result}")
        i += 1