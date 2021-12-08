print("Nhập vào số N lớn hơn 1: ") 
# Lấy dữ liệu
n = int(input())
snt = True
# Kiểm tra SNT
if (n < 2):
    ngt = False
elif (n == 2):
    snt = True
elif (n % 2 == 0):
    snt = False
else:
    # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
    for i in range(3, n, 2):
        if (n % i == 0):
            snt = False 
# In kết quả
if snt == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")