scale = input().split(',')
scale = scale[:-1]
n = int(input())
print(scale[(n%len(scale))-1])