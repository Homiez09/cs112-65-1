n = int(input("Enter height: ")) - 1 
first = (2 + (n-1)*2)*" " + "1" # a1+(n-1)*d line 1
tap = 2 + (n-2)*2 # a1+(n-1)*d เยื้อง
space = 3
spaceMax = 3 + (n-1)*4 # a1+(n-1)*d เว้นช่องข้างใน

if not n<0:
    print(first)
while n > 0:
    print(tap*" " + "1", end="")
    print(space*" " + "1")
    n -= 1
    tap -= 2
    space += 4 