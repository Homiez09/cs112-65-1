n = float(input())
check = n - int(n)

if check == 0:
  print("{} is an integer.".format(int(n)))
else:
  print("{} is not an integer.".format(n))