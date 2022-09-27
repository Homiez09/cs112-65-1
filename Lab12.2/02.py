content = input().split(",")
result = ""
for i in content:    
    result += f'"{i.strip()}",'
print(result[:-1])