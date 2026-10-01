def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a/b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    operations = {
        "1" : ("Addition", add),
        "2" : ("Subtraction", subtract),
        "3" : ("Multiplication", multiply),
        "4" : ("Division", divide),
    }

    while True:
        print("\n========== CLI CALCULATOR ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        name, operation = operations[choice]

        try:
            result = operation(a, b)
            print(f"{name}: {result:g}")
        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()