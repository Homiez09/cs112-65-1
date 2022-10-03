n = int(input())
m = [int(input()) for i in range(n)]
m.sort(reverse=True)
cash = int(input())
count = [0]*n

for i in range(len(m)):
    if cash == 0:
        break
    while cash - m[i] >= 0:
        cash -= m[i]
        count[i] += 1

for i in range(n):
    print("{0}: {1}".format(m[i], count[i]))