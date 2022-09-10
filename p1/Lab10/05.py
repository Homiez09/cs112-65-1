num = []

def sortNum(n):
    num = n
    sortNum = []
    currentNum = 0
    for i in range(len(n)):
        if num[i] > currentNum:
            currentNum = num[i]
            sortNum.append(num[i])
    return sortNum

while True:
    n = int(input())
    if n == -1:
        break
    num.append(n)

print(sortNum(num))