


     
    
print("Calculator")

a = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ").strip()
b = float(input("Enter the second number: "))

if operator == "+":
    print("The sum of two numbers is", a + b)
elif operator == "-":
    print("The difference of two numbers is", a - b)
elif operator == "*":
    print("The multiplication of two numbers is", a * b)
elif operator == "/":
    if b != 0:
        print("The division of two numbers is", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")

print("Calculator ends")