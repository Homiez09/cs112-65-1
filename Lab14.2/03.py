value = {}
result = []
print('Enter variables and values:')
while True:
    i = input()
    if i == "-1":
        break
    x = i.split("=")
    value[x[0].strip()] = x[1].strip()
print('Enter your program:')

while True:
    s = input()
    if s=='-1': 
        break
    for i in value:
        s = s.replace('{'+i+'}',str(value[i]))
    result.append(s)
print('Result:')
for i in result: 
    print(i)