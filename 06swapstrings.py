#WAP to swap first "n" characters of two strings
# second branch edits 

def swap_strings(string1, string2, n):
    if n > min (len(string1), len(string2)):
        print("Value of 'n' can't be greater than length of one or both strings.")
        return None, None
    else: 
        swapped_string1 = string2[:n] + string1[n:]    
        swapped_string2 = string1[:n] + string2[n:]
        return swapped_string1 , swapped_string2
    
try:
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    n = int(input("Enter the numbers of characters to swap: ")) 
    if n < 0 :
        print("'n' can't be negative integer.")
    else:
        result1 , result2 = swap_strings(string1, string2, n)  
        print(result1)  
        print(result2)  
    
    pass
except: 
    pass    
    