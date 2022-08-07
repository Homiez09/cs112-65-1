frame = 1
total = 0
while frame <= 10:
    print("Frame #", frame)
    scorePerFrame = int(input("  Number of pins down: "))
    total += scorePerFrame
    if scorePerFrame == 10:
        frame += 1
    else:
        print("Frame #", frame)
        scorePerFrame = int(input("  Number of pins down (0-{}): ".format(10-scorePerFrame)))
        total += scorePerFrame
        frame += 1
print("Total score is", total)
