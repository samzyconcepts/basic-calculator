def addition(firstNumber, secondNumber):
    return firstNumber + secondNumber


def subtraction(firstNumber, secondNumber):
    return firstNumber - secondNumber


def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber


def divide(firstNumber, secondNumber):
    if secondNumber == 0:
        return "Can't divide by zero"
    return firstNumber / secondNumber


def main():
    print("You are to input two values for this basic calculator")

    # Prompt user to input number
    firstNumber = int(input("Enter your first number: "))
    secondNumber = int(input("Enter your second number: "))

    # Prompt user for operator
    operator = input("Choose the operation you want to carry out (+, -, *, /): ")

    if operator == "+":
        result = addition(firstNumber, secondNumber)
        print(result)
    elif operator == "-":
        result = subtraction(firstNumber, secondNumber)
        print(result)
    elif operator == "*":
        result = multiply(firstNumber, secondNumber)
        print(result)
    elif operator == "/":
        result = divide(firstNumber, secondNumber)
        print(result)
    else:
        print("You've input an invalid operator.")


if __name__ == "__main__":
    main()
