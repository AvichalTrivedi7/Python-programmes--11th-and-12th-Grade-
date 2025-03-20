def checkPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

L = []
for i in range(1, 101):
    if checkPrime(i):
        L.append(i)

print('Prime numbers between 1 to 100:', L)
