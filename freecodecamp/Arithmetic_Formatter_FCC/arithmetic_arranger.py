def arithmetic_arranger(problems, display=True):

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if len(problems) > 4:   # First Condition
        return "Error: Too many problems."
    for key, problem in enumerate(problems):
        operand1, op, operand2 = problem.split()

        if operand1.isdigit() and operand2.isdigit() is False:  # Second Condition
            return "Error: Numbers must only contain digits."
        if op not in '+-':                                      # Third Condition
            return "Error: Operator must be '+' or '-'."
        if len(operand1) > 4 or len(operand2) > 4:              # Fourth Condition
            return "Error: Numbers cannot be more than four digits."
        if op == '+':
            answer = int(operand1) + int(operand2)
        else:
            answer = int(operand1) - int(operand2)

        if operand1 > operand2:
            dashes = len(operand1) + 2
        else:
            dashes = len(operand2) + 2

        ans_space = (dashes - len(str(answer)))

        if key < 3:
            line1 += (dashes - len(operand1)) * ' ' + operand1 + '    '
            line2 += op + (dashes - len(operand2) - 1) * ' ' + operand2 + '    '
            line3 += '-' * dashes + '    '
            line4 += ans_space * ' ' + str(answer) + '    '
        else:
            line1 += (dashes - len(operand1) +1) * ' ' + operand1
            line2 += op + (dashes - len(operand2) ) * ' ' + operand2
            line3 += '-' * (dashes + 1)
            line4 += (ans_space + 1) * ' ' + str(answer)


    if display is True:
        solution = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    else:
        solution = line1 + '\n' + line2 + '\n' + line3

    return solution
