num = int(input("Enter a number to find out whether it's prime or not: "))
ans = True

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            ans = False 
            break
    if ans :
        print(f"{num} is a prime number.") 
    else:
        print(f"{num} is not a prime number.")    
               