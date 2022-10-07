def extract_string(text) :
    ls = []
    n = ''
    for i in range(len(text)):
        n += text[i]
        if i == len(text)-1 or (text[i].isdigit() and not text[i+1].isdigit()):
            ls.append(int(n)) if n.isdigit() else ls.append(n)
            n = ''
    return ls
print(extract_string("AB12XY23"))
print( extract_string("G2X3t4") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )
