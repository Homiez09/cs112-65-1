n = int(input())
count = 0

a = 1

while a < n:
  b = 1
  while b <= a:
    if a**2 + b**2 == n**2:
      count += 1
    b += 1
  a += 1
print(count)