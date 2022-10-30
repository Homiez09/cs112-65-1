text = input()
if len(text) == 0:
    n = int(input())
    print()
num = -int(input())%len(text)
print(text[num:]+text[:num])