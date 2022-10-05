n_list = []
temp = []
def check_order(l: list):
    if n_list != []: 
        l.sort()
        global temp
        temp = temp
        print(temp)

        temp_in = temp[0]
        temp_boo = True
        for i in temp:
            if i == temp_in:
                temp_boo = True
            else:
                temp_boo = False
                break
        if temp_boo:
            return "The list is in non-increasing and non-decreasing order."
        else:
            if temp == l:
                return "The list is in non-decreasing order."
            else:
                l.sort(reverse=True)
                if temp == l:
                    return "The list is in non-increasing order."
                else:
                    return "The list is in random order."
    else:
        print([])
        return "The list is empty."

while True:
    n = int(input("Enter a number (-1 to end): "))
    if n == -1:
        break
    if int(n) >= 0 and int(n) <= 100:
        n_list.append(int(n))
        temp.append(int(n))
    else:
        print("Number is out of range.")

print("-----")
print("Original list:")
print(check_order(n_list))