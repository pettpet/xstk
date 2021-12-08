n=int(input("Nhập n="))
pet=True 
while x <= int(n/2):
    if n%x==0: # lúc này x là ước
        pet=False
        break
    x +=1 # Tăng biến lặp
if pet==True:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")