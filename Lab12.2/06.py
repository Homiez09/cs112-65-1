text = input()
if "," in text:
    text = text.split(',')
    x = ""
    if text[0].isdigit() and len(text[0]) <= 3:
        output = True
        decimal = False
        for i in range(1, len(text[1:])+1):
            if text[i].isdigit() and len(text[i]) == 3 and "." not in text[i]:
                ...
            elif "." in text[i]:
                x = text[i].split(".")
                decimal = True
                text[i] = x[0]
                if x[1].isdigit() and len(x[1]) < 3 and len(x[0]) == 3:
                    ...
                else:
                    print("ERROR")
                    output = False
                    break
            else:
                print("ERROR")
                output = False
                break
        if output:
            text = int("".join(text))
            print(str(text+1) + "." + x[1] if decimal else text+1)
    else:
        print("ERROR")
elif "." in text:
    text = text.split(".")
    if len(text) == 2:
        if text[0].isdigit() and text[1].isdigit() and len(text[1]) < 3:
            print(int(text[0])+1, text[1], sep=".")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    if text.isdigit():
        print(text+1)
    else:
        print("ERROR")