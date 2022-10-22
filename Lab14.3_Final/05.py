def abecedarian(word: str):
    word = str(word)
    if word == "":
        return 0
    result = word[0]
    for i in range(1,len(word)):
        if word[i] > result[-1]:
            result += word[i]
        else:
            break
    count = len(result)
    return count if count > 1 else 0

print(abecedarian(input()))