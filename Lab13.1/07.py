# extract_string("G2X3t4") -> ['G', 2, 'X', 3, 't', 4]
# extract_string("AB12XY23") -> ['AB', 12, 'XY', 23]
# extract_string("AB12XY23Z") -> ['AB', 12, 'XY', 23, 'Z']
# extract_string("Number 4, Privet Drive") -> ['Number ', 4, ', Privet Drive']
# extract_string("1 2 3 4 5 I love you.") -> [1, ' ', 2, ' ', 3, ' ', 4, ' ', 5, ' I love you.']
def extract_string(content):
    ls = []
    temp = ""
    for i in content:
        if i.isalpha() or i == " ":
            if temp.isnumeric():
                ls.append(int(temp))
                temp = ""
            temp += i
        elif i.isdigit():
            if temp.isalpha():
                ls.append(temp)
                temp = ""
            temp += i
        else:
            if len(temp) > 0:
                ls.append(temp)
                temp = ""
            ls.append(i)
    return ls
print(extract_string("AB12XY23Z"))
print( extract_string("G2X3t4") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )