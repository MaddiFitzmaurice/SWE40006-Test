def add_numbers(num1, num2, num3=0, number_of_inputs=2):
    if number_of_inputs == 2:
        return num1 + num2
    else:
        return num1 + num2 + num3

def main():
    print("Welcome to the Stock Calculator")
    number_of_inputs = int(input("How many numbers would you like to add? (2 or 3): "))

    if number_of_inputs != 2 and number_of_inputs != 3:
        print("Please enter 2 or 3 numbers only.")
        return

    # Collect the numbers to add
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    

    num3 = 0
    if number_of_inputs == 3:
        num3 = float(input("Enter the third number: "))

    # Perform addition
    result = add_numbers(num1, num2, num3, number_of_inputs)

    # Display result
    print(f"The result is: {result}")

    # Test 4

if __name__ == "__main__":
    main()

    hello() #attempt 2
