import math
n = int(input())
s1 = input()
s2 = input()
s = s1+s2
print("{}{}".format(s * int(n/2), s1 * int(n%2)))