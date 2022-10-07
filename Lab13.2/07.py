# Minesweeper

''' input
8x10
4
1,1
2,4
5,2
6,8 '''

''' output
1110000000
1*11110000
1111*10000
0001110000
0111000000
01*1000111
01110001*1
0000000111'''

# 1. รับข้อมูลจาก input แล้วแยกเป็น 2 ส่วน คือ ขนาดของแผนที่ และ ตำแหน่งของเมนทรีย์
# 2. สร้างแผนที่ โดยใช้ list ซ้อน list โดยให้แต่ละ list แทนแถวของแผนที่
# 3. ใช้ for loop ในการวนรอบตามจำนวนเมนทรีย์ที่รับมา
# 4. ในรอบแต่ละรอบ ให้เพิ่มค่าในแต่ละตำแหน่งของแผนที่ที่เป็นเมนทรีย์ โดยใช้ list comprehension
# 5. แสดงผลลัพธ์

l_map = input().split('x')
l_mine = int(input())
l_map = [[0 for i in range(int(l_map[1]))] for j in range(int(l_map[0]))]
for i in range(l_mine):
    l_pos = input().split(',')
    l_map[int(l_pos[0])-1][int(l_pos[1])-1] = '*'
    for j in range(int(l_pos[0])-2, int(l_pos[0])+2):
        for k in range(int(l_pos[1])-2, int(l_pos[1])+2):
            if j >= 0 and k >= 0:
                try:
                    if l_map[j][k] != '*':
                        l_map[j][k] += 1
                except:
                    pass
for i in l_map:
    print(''.join([str(j) for j in i]))
    