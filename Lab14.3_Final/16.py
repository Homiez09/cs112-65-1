text = input()
st1 = text[:len(text)//2:]
st2 = text[(len(text)//2)+1:] if len(text) % 2 else text[(len(text)//2):]
print(st1[::-1] + text[len(text)//2] + st2[::-1] if len(text)%2 != 0 else st1[::-1] + st2[::-1])