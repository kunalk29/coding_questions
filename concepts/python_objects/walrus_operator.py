# the walrus operator is used to assign and evaluate at the same time
import math

# standard assignment
x = 3

# walrus assignment
if y := 5:
    print(y)

# Useful for evaluating intermediate operations
z = (a := 4*x + 6**3) - (b := 5*math.pi)**(1.2)
print(z, a, b)