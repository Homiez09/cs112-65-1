def count_char(word):
    dic = {}
    word = word.lower()
    for i in word:
        if i.isalpha() and i not in dic:
            dic[i] = word.count(i)
    return dic

print(count_char('Hello There'))