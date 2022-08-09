h = int(input("Enter height: "))
w = int(input("Enter width: "))

if h > 0 and w > 0:
    i = 0
    while i < h:
        j = 0
        if i % 2 == 0:
            while j < w:
                print('* ',end='')
                j += 1
            print()
            j = 0
        else:
            while j < w:
                print(' *',end='')
                j += 1
            print()
            j = 0
        i += 1
else:
    print("Invalid input, program terminates.")