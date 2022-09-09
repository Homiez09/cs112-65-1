score = []

def find_mode(l):
    mode = [0]
    maxNum = 0
    for i in range(len(score)):
        if score.count(i) > maxNum:
            maxNum = score.count(i)
            mode = [i]
        elif score.count(i) == maxNum:
            mode.append(i)
    mode.sort()
    print("Mode of scores:")
    print(*mode, sep="\n")

while not len(score) == 20:
    n = int(input("Enter score: "))
    if n >= 0 and n <= 10:
        score.append(n)
    else:
        print("Score is out of range.")

print("-----")
print(f"Original list:\n{score}")
find_mode(score)