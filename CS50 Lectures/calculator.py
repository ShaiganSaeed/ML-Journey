def main():
    print("Hello User,Please Select your operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square")
    print("7. Exit")
    choice=input("Enter your choice (1-7): ")

    if choice=='1':
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        add(x,y)
        main()

    elif choice=='2':
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        subtract(x,y)
        main()

    elif choice=='3':
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        multiply(x,y)
        main()

    elif choice=='4':
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        divide(x,y)
        main()

    elif choice=='5':
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        modulus(x,y)
        main()

    elif choice=='6':
        x=int(input("Enter a number: "))
        square(x)
        main()
    elif choice=='7':
        print("\nExiting the program.")
    elif choice<'1' or choice>'7':
        print("\nInvalid choice. Please try again.")
        main()

def add(x,y):
    print(f"{x+y:,}")
def subtract(x,y):
    print(f"{x-y:,}")
def multiply(x,y):
    print(f"{x*y:,}")
def divide(x,y):
    if y==0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{x/y:,}")
def modulus(x,y):
    print(f"{x%y:,}")
def square(x):
    print(f"{x*x:,}")

main()