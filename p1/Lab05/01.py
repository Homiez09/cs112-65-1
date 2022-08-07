n = int(input())

if n > 0:
  while True:
    if n == 0:
      break
    print(n%10)
    n-=n%10
    n=n//10
else:
  print('ERROR')