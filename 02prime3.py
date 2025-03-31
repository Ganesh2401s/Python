def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def generate_primes(count):
    primes = []
    num = 2
    while len(primes)         