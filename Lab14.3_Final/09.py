n = int(input())
text = ''
for i in range(n):
    text += input()

count = ''
for i in text:
    if text.count(i) > n // 2:
        count+=i
print(count[0] if len(count) > 0 else '0')