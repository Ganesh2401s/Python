import cmath
num = 25
def is_perfect_square(num):
    result = cmath.sqrt(num)
    result = str(result)
    print(result)
    if result.find(".") == -1:
        print(f"{num} is a perfect square.")
    else :
        print(f"{num} is not a perfect square.")    
    
        
answer = is_perfect_square(16) 
 
 
print(answer)       