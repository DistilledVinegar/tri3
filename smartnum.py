#Smart Number Guesser

import math, random

class Number:
    def __init__(self, digits, primeness, square, oddness, mirrored):
        self.digits = digits
        self.primeness = primeness
        self.square = square
        self.oddness = oddness
        self.mirrored = mirrored

def isPrime(x):
    if x >= 2:
        for stench in range(2,x):
            if not (x % stench):
                return False
    else:
        return False
    return True

bung = []

for i in range(100):

    digits = len(str(i))
    
    primeness = isPrime(i)
    
    if math.sqrt(i) % 10 == 0: #check if the number cleanly squares
        square = True #math library my beloved
    else:
        square = False
        
    if i % 2 == 0:
        oddness = False
    else:
        oddness = True

    if reversed(str(i)) == str(i):
        mirrored = True
    else:
        mirrored = False

    glutton = "obj" + str(i)

    glutton = Number(digits, primeness, square, oddness, mirrored)

    bung.append(glutton)

print(bung[2].oddness)



    
