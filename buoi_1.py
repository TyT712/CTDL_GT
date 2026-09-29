def dien_tich_hcn():
    a = int(input("nhập chiều dài: "))
    b = int(input("nhập chiều rộng: "))
    s = a*b
    print (s)

dien_tich_hcn()

def giai_thua():
    n = int(input("nhập số nguyên dương: "))
    if n<0:
        print("không hợp lệ")
        return
    if n==0:
        print("giai thừa của 0 là 1")
        return
    gt = 1
    for i in range(1, n+1):
        gt *= i
    print(f"giai thừa của {n} là {gt}")

def tinh_tong():
    n = int(input("nhập số nguyên dương: "))
    if n<0:
        print("không hợp lệ")
        return
    tong = 0
    for i in range(1, n+1):
        tong += i
    print(f"Tổng từ 1 đến {n} là {tong}")
    