import math 

score = []
def find_sd(l):
    xBar = sum(l) / len(l)
    sd = 0
    for i in l:
        sd += (i - xBar) ** 2
    sd = sd / (len(l)-1)
    return math.sqrt(sd)

while True:
    n = float(input("Enter score: "))
    if n == -1:
        break 
    if n >= 0 and n <= 100:
        score.append(n)
    else:
        print("Score is out of range.")

if score:
    print("Maximum score is {:.2f}.".format(max(score)))
    print("Minimum score is {:.2f}.".format(min(score)))
    print("Average score is {:.2f}.".format(sum(score) / len(score)))
    print("Standard deviation is {:.2f}.".format(find_sd(score)))