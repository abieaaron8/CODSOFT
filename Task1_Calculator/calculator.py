print("=" * 30)
print("       CALCULATOR")
print("=" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nAvailable Operations")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operation = input("\nChoose operation: ")

if operation == "+":
    print("Result =", num1 + num2)

elif operation == "-":
    print("Result =", num1 - num2)

elif operation == "*":
    print("Result =", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation selected")