def one():
    ls = []

    while True:
        word = input()
        if word == "":
            break
        ls.append(word)

def create_factors_3_7(n):
    ls = []
    for i in range(n+1):
        if i % 3 == 0 or i % 7 == 0:
            ls.append(i)
    return ls[1:]
print(create_factors_3_7(15))