while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")

    choice = int(input("\nEnter operation: "))

    if choice == 1:
        print("Addition of two numbers is:", a + b)

    elif choice == 2:
        print("Subtraction of two numbers is:", a - b)

    elif choice == 3:
        print("Multiplication of two numbers is:", a * b)

    elif choice == 4:
        if b != 0:
            print("Division of two numbers is:", a / b)
        else:
            print("Error! Division by zero is not allowed.")

    elif choice == 5:
        if b != 0:
            print("Modulus of two numbers is:", a % b)
        else:
            print("Error! Modulus by zero is not allowed.")

    elif choice == 6:
        print("Exponentiation of two numbers is:", a ** b)

    else:
        print("Invalid choice")

    ans = input("\nDo you want to continue (y/n): ").lower()

    if ans == 'y':
        continue
    else:
        print("Thank you for using the calculator.")
        break
