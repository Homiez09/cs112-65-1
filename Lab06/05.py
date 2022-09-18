heightest = 0 
count = 0 

while True:
    n = int(input())
    if n == -1:
        break
    if heightest == 0 or n > heightest:
        heightest = n
        count += 1
print(count)