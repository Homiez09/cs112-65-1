ls = []
while True:
    n = input()
    if n == "":
        break
    ls.append(float(n))
print(ls.count(min(ls)))