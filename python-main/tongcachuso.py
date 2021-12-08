def songuyenduong(n):
    phantu = 0;
    while (n > 0):
        phantu = phantu + n % 10;
        n = int(n / 10);
    return phantu;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", songuyenduong(n));