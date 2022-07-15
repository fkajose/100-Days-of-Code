#calculator
# Add
def add(n1, n2):
    return n1 + n2

#Subtract
def minus(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": minus, "*": multiply, "/": divide}

from art import logo

def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))
    symbol_list = ""
    for symbol in operations:
        symbol_list += symbol + "  "
    print(symbol_list)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the second number? "))

    calculation_function = operations[operation_symbol]
    answer1= calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer1}")

    end = False
    while not end:
        to_continue = input(f"""
        Type 'y' to continue calculating with {answer1}, 
        'n' to start anew, or anything else to exit: """)
        if to_continue == "y":
            operation_symbol = input("Pick another operation: ")
            num3 = float(input("What is the next number? "))
            
            calculation_function = operations[operation_symbol]
            answer2 = calculation_function(answer1, num3)

            print(f"{answer1} {operation_symbol} {num3} = {answer2}")
            answer1 = answer2
        elif to_continue == "n":
            end = True
            calculator()
        else:
            end = True
        
calculator()
