#Ex.1 จงเขียน function definition ของฟังก์ชัน filter_sort_factors_3_7(ls) ที่รับ parameter เป็น List ของจำนวนเต็ม ls
#ฟังก์ชันนี้จะคืนค่า List ที่มีข้อมูล 2 ค่า
#ค่าแรกคือ List ของจำนวนเต็มบวกใน List ls ที่มี 3 หรือ 7 เป็นตัวประกอบ โดยเรียงค่าข้อมูลจากน้อยไปมาก
#ค่าที่สองคือ List ของจำนวนเต็มบวกใน List ls ที่ไม่มี 3 และ ไม่มี 7 เป็นตัวประกอบ โดยเรียงค่าข้อมูลจากมากไปน้อย
def filter_sort_factors_3_7(ls):
    first = []
    back = []
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            first.append(i)
        else:
            back.append(i)
    first.sort()
    back.sort(reverse=True)
    return [first, back]
print(filter_sort_factors_3_7([2,5,6,21,323,400]))