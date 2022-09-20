content = input().lower()
vowel = ['a','e','i','o','u']
for i in vowel:
    content = content.replace(i, i.upper())
print(content)