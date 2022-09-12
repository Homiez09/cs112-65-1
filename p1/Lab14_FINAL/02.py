f = input()
m = input()

vowel = ['a', 'e', 'i', 'o', 'u']

count = 2
species = ""
for i in range(len(f)):
    if f[i] in vowel:
        count -= 1
    if count == 0:
        break
    species += f[i]
    
for i in range(len(m)):
    if m[i] in vowel:
        species += m[i+1:]
        break
    
print(species)