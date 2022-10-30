text = input()
num = int(input())
num = -num%len(text) if len(text) != 0 else num
print(text[num:]+text[:num])