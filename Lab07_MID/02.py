space = ""

print("Upper left corner coordinate:")

x_axis_1 = int(input(f"{space:>2s}<< x axis: "))
y_axis_1 = int(input(f"{space:>2s}<< y axis: "))

xLine = int(input(f"{space:>2s}<< Eastern: "))
yLine = int(input(f"{space:>2s}<< Southern: "))

print("Enter a coordinate:")

x_axis_u = int(input(f"{space:>2s}<< x axis: "))
y_axis_u = int(input(f"{space:>2s}<< y axis: "))

x_axis_2 = x_axis_1 + xLine
y_axis_2 = y_axis_1 - yLine

if (x_axis_u >= x_axis_1) and (x_axis_u <= x_axis_2) and (y_axis_u <= y_axis_1) and (y_axis_u >= y_axis_2) :
    print(f">>> ({x_axis_u:.2f}, {y_axis_u:.2f}) is inside the rectangle.")
else:
    print(f">>> ({x_axis_u:.2f}, {y_axis_u:.2f}) is not inside the rectangle.")