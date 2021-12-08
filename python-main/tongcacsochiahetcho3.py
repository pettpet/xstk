list = []
n = int(input())

for i in range(n):
    list.append(int(input()))

a = []
for v in list:
    if v % 3 == 0:
        a.append(v)
if len(a) == 0:
    a = [0]
    print(a)
tong = 0
for v in a:
    tong += v
print(a)
print(tong)
