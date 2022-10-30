ls = []
sum_ls = []

while True:
    n = int(input())
    if n == 0:
        break
    ls.append(n)

for i in range(len(ls)):
    for j in range(len(ls)-1):
        sum_ls.append(sum(ls[i:j+2]))
print(max(sum_ls))