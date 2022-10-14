l_map = input().split('x')
l_mine = int(input())
l_map = [[0 for i in range(int(l_map[1]))] for j in range(int(l_map[0]))]
for i in range(l_mine):
    l_pos =  input().split(',')
    l_map[int(l_pos[0])][int(l_pos[1])] = '*'
    for j in range(int(l_pos[0])-1, int(l_pos[0])+2):
        for k in range(int(l_pos[1])-1, int(l_pos[1])+2):
            if j >= 0 and k >= 0:
                if int(l_pos[0]) >= 0 and int(l_pos[1]) >= 0 and int(l_pos[0]) < len(l_map) and int(l_pos[1]) < len(l_map[0]):
                    if j != len(l_map) and k != len(l_map[0]):
                        if l_map[j][k] !='*':
                            l_map[j][k] += 1

for i in l_map:
    print(''.join([str(j) for j in i]))