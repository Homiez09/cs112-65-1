content = input()
vowel = ['a','e','i','o','u']
for i in vowel:
    content = content.replace(f"{i}p{i}", f"{i}")
print(content)