"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Iterations' )
    print('5 -- Swap' )
    print('6 -- Exit' )

    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Iterations',
    5: 'Swap Numbers',
    6: 'Exit',

}
# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')
    print("A string is a data type comprised of several chars 'stringed' together.")

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')
    print(str(2+2))

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')
    print('Now printing a list!')
    for i in ['apple', 'banana', 'coconut', 'durian', 'eggplant']:
        print(i)


InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "Stores": "Walmart",
    "Phone Number": "1 (800) 925-6278",
    "Owner": "Walton Family",
    "Products":["Food","Clothes","Room Decorations","School Supplies", "Toys"]
})

InfoDb.append({
    "Stores": "Ralphs",
    "Phone Number": "1 (800) 576-43778",
    "Owner": "George Ralphs",
    "Products":["Dessert","Fruit","Vegetables","Snacks", "Ice Cream"]
})

InfoDb.append({
    "Stores": "Pacsun",
    "Phone Number": "1 (877) 372-2786",
    "Owner": " Alfred Chang and Michael Relich",
    "Products":["T-Shirts","Jeans","Shorts","Tops", "Swimsuits"]
})

InfoDb.append({
    "Stores": "Target",
    "Phone Number": "1 (800) 440-0680",
    "Owner": "Brian Cornell",
    "Products":["Food","Clothes","Appliances","Starbucks", "Toys"]
})



# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Stores"])  # using comma puts space between values
    print("\t", "Products: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Products"]))  # join allows printing a string list with separator
    print()


# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

border = "=" * 25

def iteration_tester():
    print (border)
    print("For Loop:")
    for_loop()
    print (border)
    print( "While Loop:")
    while_loop(0)  # requires initial index to start while
    print (border)
    print("Recursive Loop:")
    recursive_loop(0)  # requires initial index to start recursion
    print (border)


def swapnumbers():
    number1 = int(input(" Input First Number : "))
    number2 = int(input(" Input Second Number : "))
    print("Before Swapping: ",(number1, number2))
    # making sure that the inputs stay in order
    if number1 > number2:
        temp = number1
        number1 = number2
        number2 = temp

    print("After Swapping:",(number1, number2))

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-6: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            elif option == 4:
                iteration_tester()
            elif option == 5:
                swapnumbers()
            # Exit menu    
            elif option == 6:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 6.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()
