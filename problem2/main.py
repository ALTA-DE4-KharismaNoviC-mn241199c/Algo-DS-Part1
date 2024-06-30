def primeX(x):
    primes = []
    num = 2
    while len(primes) < x:
        if all(num%i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
        num += 1
    return primes[-1]

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29