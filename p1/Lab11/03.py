text = input()
vowel = ['a','e','i','o','u']
new_text = ""
for i in text:
    if i not in vowel and i.lower() not in vowel:
        new_text += i
print(new_text)