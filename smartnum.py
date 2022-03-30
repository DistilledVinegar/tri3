#Smart Number Guesser

import math, random

class Number:
    def __init__(self, digits, primeness, square, oddness, mirrored, value):
        self.digits = digits
        self.primeness = primeness
        self.square = square
        self.oddness = oddness
        self.mirrored = mirrored
        self.value = value

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

    value = i

    glutton = "obj" + str(i)

    glutton = Number(digits, primeness, square, oddness, mirrored, value)

    bung.append(glutton)

num_attributes = []

def questionAsker(question):
    if input(question) in ["Yes", "yes", "True", "true"]:
        num_attributes.append(True)
    else:
        num_attributes.append(False)

num_attributes.append(input("How many digits is your number? "))

questionList = ["Is your number prime? ", "Is your number square? ", "Is your number odd? ", "Is your number mirrored? "]

for question in questionList:
    questionAsker(question)

for num in bung: #Hackathon challenge: Rewrite this portion using a dictionary
    if num.digits != int(num_attributes[0]):
        bung.remove(num)
    if num.primeness != num_attributes[1] and (num in bung):
        bung.remove(num)
    if num.square != num_attributes[2] and (num in bung):
        bung.remove(num)
    if num.oddness != num_attributes[3] and (num in bung):
        bung.remove(num)
    if num.mirrored != num_attributes[4] and (num in bung):
        bung.remove(num)

for i in bung:
    print(i.value)
