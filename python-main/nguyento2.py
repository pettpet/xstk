n=int(input("Nhập n="))
pet=True 
while pet <= int(n/2):
    if n%pet==0: # lúc này x là ước
        pet=False
        break
    pet +=1 # Tăng biến lặp
if pet==True:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")
