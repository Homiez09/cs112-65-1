word = input().split(" ")
result = ""
for i in word:
    if i not in ['for', 'and', 'with', 'of']:
        result += i.capitalize() + " "
    else:
        result += i + " "

print(result)