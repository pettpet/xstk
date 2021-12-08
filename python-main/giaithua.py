def giaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
    
def giaithua_dequy(n):
    if n == 1: 
       return 1 
    else: 
        return (n * giaithua(n-1))

n = int(input("Nhập số cần tính giai thừa: "))
print(giaithua(n), " - ", giaithua_dequy(n))
