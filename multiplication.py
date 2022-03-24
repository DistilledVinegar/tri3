#multiplication table of any two difit number

num = input("What number do you want to use? ")

strnum = str(num)

digit1 = int(strnum[0])
digit2 = int(strnum[1]) #seperate the numbers

for i in range(10):
    digit1 += int(strnum[0])
    digit2 += int(strnum[1])
    print(str(digit1) + "   " + str(digit2)[0] + " " + str(digit2)[1] + "   " + "(" + str(digit1) + "+" + str(digit2)[0] + ")    " + str(digit1+int(str(digit2)[0])) + str(digit2)[1])
