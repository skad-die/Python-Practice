name = input("Input name: ").strip().title()
while True:
    try:
        age = int(input("Input age: "))
        if age < 0:
            print("Invalid age! Please try again.")
        else:
            break
    except ValueError:
        print("That's not a number")

print(f"Hello {name}, you are {age} years old.")