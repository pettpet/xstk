
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1

    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn


def fibonacci_dequy(n):
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return fibonacci_dequy(n - 1) + fibonacci_dequy(n - 2)


n = int(input('Nhap vao so nguyen duong n = '))
print(n, ' so dau tien cua day Fibonacci la:')
for i in range(0, n):
    print(fibonacci(i), " - ", fibonacci_dequy(i))