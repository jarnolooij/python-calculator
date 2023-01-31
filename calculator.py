a = int(input("Enter 1st number: "))
op = input("Enter operator: ")
b = int(input("Enter 2nd number: "))

def calculator(a, op, b):
    if op == "+":
        output = int(a + b)
    elif op == "-":
        output = int(a - b)
    elif op == "*" or op == "x":
        output = int(a * b)
    elif op == "/":
        output = int(a / b)
    return output

print('Your answer is:', calculator(a, op, b))