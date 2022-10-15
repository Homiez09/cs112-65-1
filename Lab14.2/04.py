def searchChemElement(formula: str, search: str):
    formula, search = str(formula), str(search)
    ls_ele = []
    ele = ''
    for i in formula:
        if i.isupper() and ele != '':
            ls_ele.append(ele)
            ele = i
            continue
        ele += i
    ls_ele.append(ele)
    
    for i in range(len(ls_ele)):
        if search in ls_ele[i]:
            ls_ele[i] = ls_ele[i].split(search)
            if ls_ele[i][1].isnumeric() or  ls_ele[i][1] == '':
                return ls_ele[i][1] if ls_ele[i][1] != '' else 1
            else:
                continue
        if i == len(ls_ele)-1:
            return 0

formula = input()
search = input()
print(searchChemElement(formula, search))