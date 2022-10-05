def count_factors_3_7(ls):
    count = 0
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            count += 1
    return count

def filter_factors_3_7(ls):
    first = []
    back = []
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            first.append(i)
        else:
            back.append(i)
    return [first, back]

if __name__ == "__main__":
    print()