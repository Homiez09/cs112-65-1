q = input()
x = q[1:-1]
y = input()

length_max = len(x)
count = 0

if x == "":
    print("0")
    print("0.00")
else:
    for i in y:
        count += x.count(i)
        x = x.replace(i, '')
    print(count)
    print("{:.2f}".format((count/length_max)*100))