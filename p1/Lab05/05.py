n = int(input("Enter height: ")) - 1 
tap = 2 + (n-2)*2 # a1+(n-1)*d เยื้อง
space = 3

print(((2 + (n-1)*2)*" " + "1") if not n < 0 else "")
while n > 0:   
    print(tap*" " + "1" + space*" " + "1")
    n,tap,space = n-1,tap-2,space+4