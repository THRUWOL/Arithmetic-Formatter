def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        firstLine = ""
        secondLine = ""
        dashLine = ""
        resultLine = ""
        result = 0

        def firstNumber(x): return x.split()[0]
        def operator(x): return x.split()[1]
        def secondNumber(x): return x.split()[2]
        def dashLength(x): return len(str(max(int(firstNumber(x)), int(secondNumber(x))))) + 2
        def firstOrSecond(x): return True if len(firstNumber(x)) >= len(secondNumber(x)) else False
        def spaceBeforeTheFirstNumber(x): return 2 if firstOrSecond(x) else len(secondNumber(x))-len(firstNumber(x)) + 2
        def spaceBeforeTheSecondNumber(x): return len(firstNumber(x))-len(secondNumber(x))+1 if firstOrSecond(x) else 1
        def spaceBeforeTheResult(x): return dashLength(x) - len(str(result))
        def output(): return f"{firstLine.rstrip()}\n{secondLine.rstrip()}\n{dashLine.strip()}\n{resultLine.rstrip()}" if solve else f"{firstLine.rstrip()}\n{secondLine.rstrip()}\n{dashLine.strip()}"

        for problem in problems:
            if not firstNumber(problem).isdigit() or not secondNumber(problem).isdigit():
                return "Error: Numbers must only contain digits."
            if operator(problem) not in '+-':
                return "Error: Operator must be '+' or '-'."
            if len(firstNumber(problem)) > 4 or len(secondNumber(problem)) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            if len(firstLine) == 0:
                firstLine += ' ' * spaceBeforeTheFirstNumber(problem) + firstNumber(problem)
            else:
                firstLine += ' ' * 4 + ' ' * spaceBeforeTheFirstNumber(problem) + firstNumber(problem)
            if len(secondLine) == 0:
                secondLine += operator(problem) + ' ' * spaceBeforeTheSecondNumber(problem) + secondNumber(problem)
            else:
                secondLine += ' ' * 4 + operator(problem) + ' ' * spaceBeforeTheSecondNumber(problem) + secondNumber(problem)
            if len(dashLine) == 0:
                dashLine += '-' * dashLength(problem)
            else:
                dashLine += ' ' * 4 + '-' * dashLength(problem)

            if solve:
                if operator(problem) == '+':
                    result = int(firstNumber(problem)) + int(secondNumber(problem))
                    resultLine += ' ' * spaceBeforeTheResult(problem) + str(result) + ' ' * 4
                else:
                    result = int(firstNumber(problem)) - int(secondNumber(problem))
                    resultLine += ' ' * spaceBeforeTheResult(problem) + str(result) + ' ' * 4

        return output()
