import math

def first():
    h = int(input("Enter number of hours: "))
    m = int(input("Enter number of minutes: "))
    if h >= 0 and m >= 0 and m < 60 and h < 24:
        minute = (h*60)+m
        price = 0
        if minute > 120:
            minute -= 120
            price += 10
            minute = math.ceil(minute/60)
            price += minute * 10
            print(f"Total amount due is {price} Bahts.")
        elif minute == 120:
            price += 10
            print(f"Total amount due is {price} Bahts.")
        elif minute > 15 and minute < 120:
            price += 10
            print(f"Total amount due is {price} Bahts.")
        else:
            print("No charge, thanks.")
    else:
        print("Input Error!")

def second():
    h = int(input("Enter number of hours: "))
    m = int(input("Enter number of minutes: "))
    minute = (h*60) + m
    price = 0
    if h >= 0 and m >= 0 and m < 60 and h < 24:
        if minute <= 15:
            print(f"No charge, thanks.")
        elif minute > 15 and minute < 121:
            price += 10
            print(f"Total amount due is {price} Bahts.")
        else:      
            price = ((math.ceil(minute/60)-2) * 10) + 10
            print(f"Total amount due is {price} Bahts.")
    else:
        print("Input Error!")

if __name__ == '__main__':
    first()