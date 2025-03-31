# Quadratic equation ==> ax² + bx + c
import cmath
a, b, c = 1, 13, 42
# Discriminant ==> b² - 4ac
dis = (b**2) - (4 * a * c)
#Values of Roots 
root1 = (-b + cmath.sqrt(dis)) / 2 * a
root2 = (-b - cmath.sqrt(dis)) / 2 * a

print(root1)    # Output = -6+0j
print(root2)    # Output = -7+0j

