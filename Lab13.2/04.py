def checkDay(m:int, d:int):
    global sunday
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m >= 0 and m <= 12:
        if d < 1 or d > days[m-1] or sunday > 31 or sunday < 1:
            return True
    return False

def checkError(s_date:list, e_date:list):
    error = False
    if int(s_date[1]) < 1 or int(s_date[1]) > 12 or int(e_date[1]) < 1 or int(e_date[1]) > 12:
        print("Wrong Month")
        error = True
    if checkDay(int(s_date[1]), int(s_date[0])) or checkDay(int(e_date[1]), int(e_date[0])):
        print("Wrong Day")
        error = True
    return error

s_date = input().split("-")
e_date = input().split("-")
sunday = int(input())

if checkError(s_date, e_date):
    pass
else:
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    count = 0
    s, e = 0, 0
    for i in days[:int(s_date[1])-1]:
        s += i
    for i in days[:int(e_date[1])-1]:
        e += i
    ls = [s+int(s_date[0]), e+int(e_date[0])]
    ls.sort()
    print(ls)
    for i in range(sunday, 365, 7):
        if i >= ls[0] and i <= ls[1]:
            count += 1
    print(count)
