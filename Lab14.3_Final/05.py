def abecedarian(word: str):
    word = str(word).lower()
    if word == "":
        return 0
    result = word[0]
    for i in range(1,len(word)):
        if word[i] > result[-1]:
            result += word[i]
        elif word[i] == result[-1]:
            pass
        else:
            break
    count = len(result)
    return count

print(abecedarian(input()))