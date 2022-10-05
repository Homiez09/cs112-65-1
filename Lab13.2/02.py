n = int(input())
score = []
for i in range(n):
    x = input()
    f, k = ['A', 'Q', 'J', 'K'], [1,10,10,10]
    for i in range(4):
        x = x.replace(f[i], str(k[i]))
    x = x.split()
    temp, i = 0, 0
    while i < len(x):
        if temp > 16:
            break
        temp += int(x[i])
        i += 1
    score.append(temp) if temp <= 21 else score.append("busted")

print(*score, sep="\n")