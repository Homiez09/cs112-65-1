text = input()
vowel = ['a','e','i','o','u']
count = 0
for i in text:
    if i.lower() in vowel:
        count += 1
print(count)