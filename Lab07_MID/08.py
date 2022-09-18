weekday = input()
days = int(input())
day = days
x = 0
if weekday == "Sunday":
    x = 1
elif weekday == "Monday":
    x = 2
    day += 2
elif weekday == "Tuesday":
    x = 3
    day += 4
elif weekday == "Wednesday":
    x = 4
    day += 6
elif weekday == "Thursday":
    x = 5
    day += 8
elif weekday == "Friday":
    x = 6
    day += 10
elif weekday == "Saturday":
    x = 7
    day += 12
else:
    x = 0

if x > 7 or x < 1 or days > 31 or days < 1:
    print("ERROR")
else:
    day -= x
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
