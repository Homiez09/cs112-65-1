n = int(input())
ans = 1

while not n == 0:
    x = n % 10
    if (n % 10) % 2 == 0:
        ans *= x
    n //= 10
if ans == 1:
    ans =- 1
print(ans)  