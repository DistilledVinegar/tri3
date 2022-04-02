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

    glutton = Number(digits, primeness, square, oddness, mirrored, value)

    bung.append(glutton)

def questionAsker(question):
    answer = input(question)
    while answer not in ["yes", "no", "Yes", "No"]:
        print("no no no this is ALL wrong")
        answer = input(question)
    return answer
        
questionList = ["Is your number prime? ", "Is your number square? ", "Is your number odd? ", "Is your number mirrored? "]

digits = int(input("How many digits is your number? "))
for num in bung: 
    if num.digits != digits:
        print("removing " + str(num.value))
        bung.remove(num)
        print(len(bung))
        
primeness = questionAsker(questionList[0])
for num in bung: 
    if num.primeness != primeness:
        print("removing " + str(num.value))
        bung.remove(num)

squareness = questionAsker(questionList[1])
for num in bung: 
    if num.square != squareness:
        print("removing " + str(num.value))
        bung.remove(num)
        
oddness = questionAsker(questionList[2])
for num in bung: 
    if num.oddness != oddness:
        print("removing " + str(num.value))
        bung.remove(num)
        
mirrored = questionAsker(questionList[3])
for num in bung: 
    if num.mirrored != mirrored:
        print("removing " + str(num.value))
        bung.remove(num)

"""for num in bung: #Hackathon challenge: Rewrite this portion using a dictionary
    if num.digits != digits:
        bung.remove(num)
    elif num.primeness != primeness:
        bung.remove(num)
    elif num.square != squareness:
        bung.remove(num)
    elif num.oddness != oddness:
        bung.remove(num)
    elif num.mirrored != mirrored:
        bung.remove(num)"""

for i in bung:
    print(i.value)
