def namelist(names):
    if names == []:
        return ''
    elif len(names) == 1:
        return names[0]
    else:
        return ", ".join(names[:-1]) + " & " + names[-1]
        
print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )