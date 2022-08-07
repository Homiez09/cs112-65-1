from sre_constants import MIN_UNTIL


maxN = 0
minN = 0
sumN = 0
count = 0
checkFirst = False

while True:
    n = input() 
    if n == "":
        break
    n = float(n)

    if checkFirst == False:
        minN = n
        checkFirst = True
    elif n > maxN:
        maxN = n
    elif n < minN:
        minN = n

    count += 1
    sumN += n
print(minN, maxN)
if maxN < minN:
    maxN, minN = minN, maxN

print(f"{maxN:.2f} {minN:.2f}")
print(f"{sumN:.2f} {(sumN/count):.2f}")