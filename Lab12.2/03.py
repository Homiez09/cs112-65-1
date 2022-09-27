data = []
len_of_first = 0
i = 0

while True:
    n = input()
    if n == "-1": break
    data.append(n.split('=',1))
    if len(data[i][0].strip()) > len_of_first:   
        len_of_first = len(data[i][0].strip())
    i += 1

for i in data:
    print(i[0].strip().rjust(len_of_first) + ' = ' + i[1].strip())