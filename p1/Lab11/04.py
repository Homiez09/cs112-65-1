word = input()
count = 0
while True:
    x = input()
    if x == "0":
        break
    count += word.count(x)
    word = word.replace(x, "")
print(f"{count}/{len(word)+count}")