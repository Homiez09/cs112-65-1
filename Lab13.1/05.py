def one():
    ls = input().split(".")
    return ls

def two():
    # Ex.2 เขียนโปรแกรมรับสตริงมา 1 ค่า ซึ่งประกอบด้วยจำนวนเต็มหลายค่า ซึ่งมี . เป็นตัวคั่น แล้วแยกสตริงตามตัวคั่นเป็น List ของจำนวนเต็ม ls
    content = input().split(".")
    ls = [int(i) for i in content if i != ""]
    return ls

def three():
    ls1 = input().split(",")
    ls2 = input().split(",")
    print(f"{float(ls1[0]) + float(ls2[0])},{float(ls1[1]) + float(ls2[1])}")

if __name__ == '__main__':
    #print(one())
    #print(two())
    three()