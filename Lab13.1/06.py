ls = []
while True:
    content = input()
    if content == "":
        break
    ls.append(content)
print("".join(ls))