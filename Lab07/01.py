n = int(input("Enter a number: "))
i = 0
ans = ""
if n > 0 and n <= 26:
    while True:
        if i == n:
            break
        ans += chr(65+i)
        print(ans)
        i += 1
else:
    print("Invalid input, program terminates.")