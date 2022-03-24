#multiplication table of any two difit number

nums = [87, 38, 76, 19, 78, 49, 67]

for i in nums:
    print("Now doing: " + str(i))
    strnum = str(i)
    digit1 = int(strnum[0])
    digit2 = int(strnum[1]) #seperate the numbers
    for j in range(10):
        digit1 += int(strnum[0])
        digit2 += int(strnum[1])
        print(str(digit1) + "   " + str(digit2)[0] + " " + str(digit2)[1] + "   " + "(" + str(digit1) + "+" + str(digit2)[0] + ")    " + str(digit1+int(str(digit2)[0])) + str(digit2)[1])
