import math

def shoot(dmg: int, targets: list):
    count = [0]
    for i in targets:
        count.append(count[-1] + int(math.ceil(int(i)/dmg)))
    print(count[-1])
    print(*count[1:])

dmg = int(input())
targets = input().split()
shoot(dmg, targets)