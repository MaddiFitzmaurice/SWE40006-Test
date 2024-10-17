import os

def add_numbers(num1, num2, num3=0, number_of_inputs=2):
    if number_of_inputs == 2:
        return num1 + num2
    else:
        return num1 + num2 + num3

def main():
    print("Welcome to the Stock Calculator")

    # Check if running in an interactive mode or CI mode
    if os.getenv('CI', 'false') == 'true':
        # Use default values when running in CI (like Jenkins)
        print("Running in CI mode")
        number_of_inputs = 2
        num1 = 10
        num2 = 20
        num3 = 0
    else:
        # Collect user input when running locally
        number_of_inputs = int(input("How many numbers would you like to add? (2 or 3): "))
        if number_of_inputs != 2 and number_of_inputs != 3:
            print("Please enter 2 or 3 numbers only.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if number_of_inputs == 3:
            num3 = float(input("Enter the third number: "))
        else:
            num3 = 0

    # Perform the calculation
    result = add_numbers(num1, num2, num3, number_of_inputs)
    print(f"The result is: {result}")

if __name__ == "__main__":
    print(5/0)
    main()