# WAP to generate list of prime numbers upto n

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

try: 
    n = int(input("Enter a number upto which you want to generate prime numbers: "))
    if n < 2:
        print("No prime number below 2.")
    else:
        primes = [i for i in range(2,n+1) if is_prime(i)]
        print(primes)  
except ValueError :
    print("Enter a valid integer.")
     