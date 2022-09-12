word = input()
count = 1

if len(word) == 1:
    pass
elif word == '':
    count -= 1
else:
    for i in range(len(word)-1):
        if word[i+1] > word[i]:
           count += 1
        else:
            break 
print(count) 