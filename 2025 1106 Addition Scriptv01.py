print("Hello and welcome to the script!!!")

"""
Variable 

"""
a = 0
b = 0
c = 0
d = 0


def QuitFunction():
    print("Thank you for using the script!")
    exit()  # This will exit the program


def HelloFuction():
    print("\nThis script will add two numbers together!")
    
    a = int(input("\nWhat do you want a to be (number): "))
    b = int(input("\nWhat do you want b to be (number): "))

    c = a + b
    print(f"\nThe given answer to your problem is", c)

HelloFuction() #runs the function

# print(c, " this the default value in the code") #hash for line to work

while True:
    X = input("\nEnter 'add' to add numbers or 'quit' to exit: ").lower()
    if X == "quit":
        QuitFunction()
    elif X == "add":
        HelloFuction()
    else:
        print("\nInvalid input. Please try again.")


