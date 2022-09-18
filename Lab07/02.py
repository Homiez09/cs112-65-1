n = int(input("Enter a number: "))
i = 0
j = 0
ans = ""

if n > 0 and n <= 26:
    while i < n:
        ans = ""
        if i == n: 
            break
        j = 0
        while j < n-i:
            ans += chr(65+j)
            j += 1
        print(ans)
        i += 1
else:
    print("Invalid input, program terminates.")