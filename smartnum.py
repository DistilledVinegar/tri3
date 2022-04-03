#rewrite of numguesser
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

questionList = ["Is your number prime? ", "Is your number square? ", "Is your number odd? ", "Is your number mirrored? "]
def questionAsker(question):
    answer = input(question)
    while answer not in ["yes", "no", "Yes", "No"]:
        print("no no no this is ALL wrong")
        answer = input(question)
    if answer in ["yes", "Yes"]:
        return True
    else:
        return False

bung = [] #two separate dictionaries have to be used or else it will skip number after removing them causing it to break :/
sniff = []

for i in range(10000): #this is very important i think
    bung.append(Number(len(str(i)), isPrime(i), eval("math.sqrt(i)*10 % 10 == 0"), eval("i % 2 == 1"), eval("str(i)[::-1] == str(i)"), i))

digits = int(input("How many digits is your number? "))
for i in bung:
    if i.digits == digits:
        sniff.append(i)

def narrow(attribute, answer):
    global bung
    global sniff
    bung = sniff
    sniff = []
    for i in bung:
        print("Checking: " + str(i.value))
        gulch = 'i.' + attribute
        if eval(gulch) == answer:
            print("Appending: " + str(i.value))
            sniff.append(i)
        
narrow("primeness", questionAsker(questionList[0]))
narrow("square", questionAsker(questionList[1]))
narrow("oddness", questionAsker(questionList[2]))
narrow("mirrored", questionAsker(questionList[3]))

for i in sniff:
    print(str(i.value))
