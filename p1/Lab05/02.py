price = 0

if hours >= 0 and minutes >= 0 and minutes <= 59 and hours <= 20 and not(hours == 20 and minutes > 0):
    if minutes > 0:
        hours += 1

    if buyAmt >= 3001:
        pass
    elif buyAmt >= 300 and buyAmt <= 3000:
        price = (hours-4)*50
    elif hours >= 3 and hours <= 4:
        price = (hours-2)*20
    else:
        price = ((hours-4)*50)+40

    if price > 0:
        print(f"Total amount due is {price} Baht, thank you.")
    else:
        print("No charge, thank you.")
else:
    print("Invalid time.")