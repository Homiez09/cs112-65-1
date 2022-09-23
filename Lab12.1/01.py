long_text = 0
def one():
    while True:
        text = input()
        if text == "": break
        if len(text) > long_text: long_text = len(text)
    print(long_text)

def two():
    long_text = 0
    content = ""
    while True:
        text = input()
        if text == "": break
        if len(text) > long_text: 
            long_text = len(text)
            content = text
    print(content)