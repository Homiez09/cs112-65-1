n = int(input())
i = 1
lowest = 100000000
while i <= n:
    j = 1
    while j <= n:
        chk = i * j
        if chk == n:
            if i + j <= lowest:
                lowest = i + j
        j += 1
    i += 1
print(lowest)