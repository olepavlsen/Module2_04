numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
no_primes = []
for i in range(1, 15):
    a = numbers[i]
    for j in range(1, (a//2)+1):
        b = numbers[j]
        c = a % b
        if c == 0 and a != b:
            no_primes.append(numbers[i])
numbers.remove(1)
setN = set(numbers)
setNP = set(no_primes)
setP = setN.difference(setNP)
primes = list(setP)
no_primes = list(setNP)
print('Primes:', primes)
print('Not primes:', no_primes)