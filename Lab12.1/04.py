def one():
    content = input()
    upper = 0
    lower = 0
    for i in content:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print(lower)
    print(upper)

def two():
    content = input() 
    new_content = ""
    for i in content:
        if i.isupper():
            new_content += i.lower()
        else:
            new_content += i.upper()
    print(new_content) 

one()