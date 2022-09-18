x = int(input())

for i in range(1, x*2, 2):
    star = "*"*i
    result = f"|{star.center((x*2)-1)}|"
    print(result)