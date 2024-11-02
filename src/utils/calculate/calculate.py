from src.utils.calculate.is_number import is_number
from src.utils.calculate.is_operator import is_operator
from src.utils.calculate.infix_to_postfix import infix_to_postfix


def calculate(string: str):
    postfix_lst = infix_to_postfix(string)
    postfix_stc = []

    OPERATOR = {"+", "-", "*", "/", "%", "^"}

    for value in postfix_lst:
        if value in OPERATOR:
            b = postfix_stc.pop()
            a = postfix_stc.pop()

            if value == "+":
                result = a + b
            elif value == "-":
                result = a - b
            elif value == "*":
                result = a * b
            elif value == "/":
                result = a / b
            elif value == "%":
                result = a % b
            elif value == "^":
                result = pow(a, b)

            postfix_stc.append(result)
        else:
            postfix_stc.append(value)

    return postfix_stc[0]


    


