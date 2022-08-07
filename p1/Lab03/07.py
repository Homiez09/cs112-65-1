import math

x = float(input("Enter x : "))
result = "f({:.2f}) = ".format(x)
if x > 99:
    cal = (2*(x**3)) - (x/math.sqrt(x+1))
    result += "{}".format(math.ceil(cal))
elif x > 0:
    cal = (3*(x**2))-((1-x)**2)
    result += "{}".format(math.ceil(cal))
elif x < 0:
    cal = math.sqrt((x**2)+1)
    result += "{:.0f}".format(math.ceil(cal))
else:
    cal = x
    result += "{:.0f}".format(math.ceil(cal))

print(result)

