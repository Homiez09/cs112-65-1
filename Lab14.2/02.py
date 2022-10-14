def cloth_size(width_list):
    size = {'S': 0, 'M': 0, 'L': 0}
    for i in width_list:
        if i > 44:
            size["L"] += 1
        elif i > 36:
            size["M"] += 1
        else:
            size["S"] += 1 
    return size
    
print(cloth_size([50, 44, 40, 48]))
#{'S': 0, 'M': 2, 'L': 2}
