def decode(source: str, key: str, code: str):
    source, key, code = str(source).replace(" ", ""), str(key), str(code)
    new_source = ""
    for i in source:
        if i not in new_source:
            new_source += i
    result = ""
    for i in code:
        k = key.find(i)
        result += new_source[k] if k != -1 else i
    return result

print(decode(input(), input(), input()))