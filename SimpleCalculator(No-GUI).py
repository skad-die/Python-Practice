print("Simple Calculator (NO GUI)")
print("[1] Addition\t[2] Subtraction\t[3] Multiplication\t[4] Division\n\n[HELP] Display Options\n[EXIT] Quit Program")
while True:
    userInput = input("\nInput: ").strip().upper()

    try:
        match userInput:
            case "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a + b)

            case "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a - b)

            case "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a * b)

            case "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", a / b)

            case "EXIT":
                print("Program Terminated.")
                break

            case "HELP":
                print("[1] Addition\t[2] Subtraction\t[3] Multiplication\t[4] Division\n[EXIT] Quit\t[HELP]")

            case _:
                print("Invalid Input. Type HELP for options.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")