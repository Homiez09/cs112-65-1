n = int(input())
closest = []
x = 9999999
y = []
for i in range(n):
  m = int(input())
  closest.append(m)

closest.sort()
for i in range(len(closest) -1):
  diff = closest[i+1] - closest[i]
  if diff < x:
    x = diff
    y = [[closest[i+1], closest[i]]]
  elif diff == x:
    y.append([closest[i+1], closest[i]])

for i in y:
  i.sort()
  print(*i)