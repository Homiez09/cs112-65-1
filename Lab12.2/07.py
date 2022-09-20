spe = '-_=.$'
content = input()
for i in spe:
    content = content.replace(i, '!')

content = content.split('!')
new_content = content.pop(0).lower()
for i in content: 
    new_content += i.capitalize()
print(new_content)