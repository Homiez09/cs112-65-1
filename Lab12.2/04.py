content = input()
file_ex = ""
if not content.rfind('.') == -1:
    file_ex = content[content.rfind('.'):]
    file_ex = file_ex[1:]

if len(content) > 15:
    content = content[:15]

forbidden = [' ', '\\', '/', ':', '*', '"', '<', '>', '|', '.']
for i in forbidden:
    content = content.replace(i, '_')
for i in forbidden:
    file_ex = file_ex.replace(i, '_')

if len(file_ex) > 3:
    file_ex = file_ex[:3]

if file_ex in content and file_ex != "":
    print(content[:-len(file_ex)-1] + f".{file_ex}")
elif not file_ex == "":
    print(content + f".{file_ex}")
else:
    print(content)