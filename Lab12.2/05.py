content = input()
correct = []
while True:
    guess = input()
    if guess ==  "0": break
    if guess in content: correct.append(guess)
for i in content: 
    print(i if i in correct else "-", end="")