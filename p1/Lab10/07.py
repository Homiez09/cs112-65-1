nExam = int(input())
base = float(input())
nStudent = int(input())

count = 0
text = []
for i in range(nStudent):
    s = int(input())
    percent = (s/nExam)*100
    if percent >= base:
        text.append(f'{i+1} {percent:.2f}')
    else:
        count += 1
        text.append(f'({i+1}) {percent:.2f}')
print(count)
print(*text, sep="\n")
