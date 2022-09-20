content = input()
new_content = ""
while True:
    if len(content) < 3:
        new_content += content
        break
    if content[0] == content[2] and content[1] == 'p':
        new_content += content[0]
        content = content[3:]
    else:
        new_content += content[0]
        content = content[1:]
print(new_content)
