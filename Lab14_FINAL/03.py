def mixName(n1, n2):
    vowel = ['a', 'e', 'i', 'o', 'u']
    species = ""

    count = 2
    for i in range(len(n1)):
        if n1[i] in vowel:
            count -= 1
        if count == 0:
            break
        species += n1[i]

    count = 1
    for i in range(len(n2)):
        if n2[i] in vowel:
            count -= 1
        if count == 0:
            species += n2[i+1:]
            break
    
    if count == 1:
        species += n2
    
    return species
    
print(mixName(input(), input()))
