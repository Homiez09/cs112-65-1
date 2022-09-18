text = input()
result = []
new_result = []
for i in range(len(text) - 1):
    result.append((text[i]+text[i+1]).lower())
for i in range(len(result)):
    if result[i] not in new_result:
        new_result.append(result[i])
new_result.sort()
print(*new_result, sep="\n")