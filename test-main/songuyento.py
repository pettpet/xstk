print("Nhập vào số N lớn hơn 1: ") 
# Lấy dữ liệu
n = int(input())
flag = True
# Kiểm tra SNT
if (n < 2):
    flag = False
elif (n == 2):
    flag = True
elif (n % 2 == 0):
    flag = False
else:
    # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
    for i in range(3, n, 2):
        if (n % i == 0):
            flag = False 
# In kết quả
if flag == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")