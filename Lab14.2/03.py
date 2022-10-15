def translate(ls: list):
    ls_dict = {}
    for i in ls:
        x = i.split("=")
        ls_dict[x[0].strip()] = int(x[1].strip())
    return ls_dict
    
def export(var: list, code: list):
    var = translate(var)
    result = []
    for i in code: 
        content = i

        for j in var:
            if j in content: 
                content = content.replace(f"{chr(123)}{j}{chr(125)}", str(var[j]))
        result.append(content)
    return result
            
if __name__ == "__main__":
    print("Enter variables and values:")
    var = []
    while True:
        var.append(input())
        if var[-1] == "-1":
            break

    print("Enter your program:")
    code = []
    while True:
        code.append(input())
        if code[-1] == "-1":
            break
    print("Result:")
    print(*export(var[:-1], code[:-1]), sep="\n")