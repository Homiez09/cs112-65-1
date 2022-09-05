score = []
star = [0]*11

def addList(n):
    star[n] += 1
    score.append(n)

for i in range(20):
    n = int(input("Enter score: "))
    if n >= 0 and n <= 10:
        addList(n)
    else:
        print("Score is out of range.")    
        n = int(input("Enter score: "))
        addList(n)

print("Original list: ")
print(score)
for i in range(len(star)):
    print("{:>2d} {}".format(i, "*"*star[i]))