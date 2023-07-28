# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
a = int(input())
b = int(input())
c = ((a**2)+(b**2))**0.5
print(c)
d = c//2
print(d)
e = d/b
print(e)
f = cmath.asin(e)
print(f)
g = cmath.phase(complex(f))
print(g)