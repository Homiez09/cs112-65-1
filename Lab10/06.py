def remove_duplicates(t):
    data = list(t)
    newData = []
    for i in range(len(data)):
        if data[i] not in newData:
            newData.append(data[i])
    return(newData)

remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4])
#[1, 2, 3, 4]
remove_duplicates(['a', 'b', 'c', 'e', 'f'])
#['a', 'b', 'c', 'e', 'f']
remove_duplicates([2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3])
#[2, 1, 3]