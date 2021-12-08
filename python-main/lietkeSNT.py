import math
 
def snt(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:");
sb = "";
if (n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (snt(i)):
        sb = sb + str(i) + " ";
    i = i + 2;
print(sb);