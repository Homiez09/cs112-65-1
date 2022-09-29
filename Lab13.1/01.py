def one():
    ls = []

    while True:
        word = input()
        if word == "":
            break
        ls.append(word)

def create_factors_3_7(n):
    ls = []
    i = 1
    while len(ls) < n:
        if i % 3 == 0 or i % 7 == 0:
            ls.append(i)
        i += 1
    return ls
print(create_factors_3_7(16))
