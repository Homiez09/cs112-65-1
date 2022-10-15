def count_char(word):
    dic = {}
    word = word.lower()
    for i in word:
        if i in dic.keys():
            dic[i] +=1        
        elif i.isalpha() :
            dic[i] = 1
    return dic

print(count_char('Hello There'))