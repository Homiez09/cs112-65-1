sunday = int(input())
day = int(input())

if sunday > 7 or sunday < 1 or day > 31 or day < 1:
    print("ERROR")
else:
    day -= sunday
    result = (day % 7) + 1
    if result == 1:
        print("Sunday")
    elif result == 2:
        print("Monday")
    elif result == 3:
        print("Tuesday")
    elif result == 4:
        print("Wednesday")
    elif result == 5:
        print("Thursday")
    elif result == 6:
        print("Friday")
    elif result == 7:
        print("Saturday")