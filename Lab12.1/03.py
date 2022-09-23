i = 1
result = ""
while True:
    content = input()
    if content == "": break 
    if i % 2 == 0:
        result += min(content)
    else:
        result += max(content)
    i += 1
print(result)