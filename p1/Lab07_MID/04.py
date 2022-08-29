direction = ""
while True:
    print("<<Point a>>")
    aX = int(input("Enter x coordinate: "))
    bX = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    aY = int(input("Enter x coordinate: "))
    bY = int(input("Enter y coordinate: "))
    if aX == 0 and aY == 0 and bX == 0 and bY == 0:
        break

    if aX > 0 and aY > 0 and bX > 0 and bY > 0:
        direction = "north-east"
    elif aX > 0 and aY > 0 and bX < 0 and bY > 0:
        direction = "south-east"
    elif aX > 0 and aY > 0 and bX < 0 and bY < 0:
        direction = "south-west"
    elif aX > 0 and aY < 0 and bX > 0 and bY < 0:
        direction = "north-west"
    elif aX == bX and bY > aY:
        direction = "north"
    elif aY == bY and bX > aX:
        direction = "east"

    print(f"Distance between ({aX}, {bX}) and ({aY}, {bY}):")
    print(f"Euclidean distance is {((aX - bX)**2 + (aY - bY)**2)**(1/2)}.")
    print(f"Horizontal distance is {abs(aX - bX)}.")
    print(f"Vertical distance is {abs(aY - bY)}.")
    print(f"we are going {direction}.")

