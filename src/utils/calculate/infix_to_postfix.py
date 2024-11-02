# Function to return precedence of operators
def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*' or c == "%":
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Function to perform infix to postfix conversion
def infix_to_postfix(s):
    st = []
    result = []
    operand_str = ""

    for i in range(len(s)):
        c = s[i]

        # If the scanned character is
        # an operand, add it to the output string.
        if (c >= '0' and c <= '9'):
            operand_str += c
        elif (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            raise ArithmeticError("Only number and operator are allowed!")

        # If the scanned character is an
        # ‘(‘, push it to the stack.
        elif c == '(':
            if operand_str != "":
                result.append(int(operand_str))
                operand_str = ""
            st.append('(')

        # If the scanned character is an ‘)’,
        # pop and add to the output string from the stack 
        # until an ‘(‘ is encountered.
        elif c == ')':
            if operand_str != "":
                result.append(int(operand_str))
                operand_str = ""
            while st[-1] != '(':
                result.append(st.pop())
            st.pop()

        # If an operator is scanned
        else:
            if operand_str != "":
                result.append(int(operand_str))
                operand_str = ""
            while st and (prec(c) < prec(st[-1]) or prec(c) == prec(st[-1])):
                result.append(st.pop())
            st.append(c)
    
    if operand_str != "":
        result.append(int(operand_str))
        operand_str = ""

    # Pop all the remaining elements from the stack
    while st:
        result.append(st.pop())

    return result
