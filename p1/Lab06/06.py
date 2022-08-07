n = int(input())
sumN = 0 

while True:
    sumN += n%10
    n -= n % 10
    n //= 10
    if n == 0:
        n = sumN
        if int(sumN/10) == 0:
            break
        sumN = 0
print(sumN)