numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []
for i in numbers:
    k = 0
    for j in range(1, i+1):
        if i % j == 0:
            k += 1
    if k == 2:
        primes.append(i)
    elif i != 1:
        no_primes.append(i)
print('Primes:', primes)
print('Not primes:', no_primes)