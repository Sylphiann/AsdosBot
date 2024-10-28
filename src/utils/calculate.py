import is_number
import is_operator

def calculate(string: str):
    string = string.replace(" ", "")
    first_index = 0
    last_index = 0
    is_operand = True

    operands = []
    operators = []

    for chr in string:
        if is_number(chr):
            if (is_operand):
                last_index += 1
            else:
                operand = int(string[first_index:last_index])
                operands.append(operand)
                first_index = last_index + 1
        elif is_operator(chr):
            if (not is_operand):
                last_index += 1
            else:
                operator = string[first_index:last_index]
                operators.append(operator)
                first_index = last_index + 1

    if (is_operand):
        operand = int(string[first_index:last_index])
        operands.append(operand)
    else:
        operator = string[first_index:last_index]
        operators.append(operator)

    operands.reverse()
    operators.reverse()

    while len(operators) != 0:
        operator = operators[len(operators) - 1]
        operand1 = operands[len(operands) - 1]
        operand2 = operands[len(operands) - 2]
        result = None

        if (operator == "+"):
            result = operand1 + operand2
        elif (operator == "-"):
            result = operand1 - operand2
        elif (operator == "*"):
            result = operand1 * operand2
        elif (operator == "/"):
            result = operand1 / operand2
        elif (operator == "^"):
            result = pow(operand1, operand2)

        operators.pop()
        operands.pop()
        operands[len(operands) - 1] = result

    return operands[0]

    


