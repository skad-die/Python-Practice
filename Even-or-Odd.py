print("Input a number to check if it's even or odd. (Type 'EXIT' to quit)")
while True:
    userInput = input("Input a number: ").strip().upper()

    if userInput == "EXIT":
        print("Program Terminated!")
        break

    try:
        number= int(userInput)
        if number % 2 == 0:
            print(f"The number {number} is Even.")
        else:
            print(f"The number {number} is Odd.")

    except ValueError:
        print("That's not a number. Please enter a digit or 'EXIT'.")