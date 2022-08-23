n = int(input())
ans = 0

while not n == 0:
    x = n % 10
    if not (n % 10) % 2 == 0:
        ans += x
    n //= 10
if ans == 0:
    ans =- 1
print(ans)  