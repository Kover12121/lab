def calculate(s):
    tokens = []
    i = 0

    while i < len(s): # разбивает вводимую строку на токены
        if s[i].isspace():
            i += 1
        elif s[i].isdigit() or s[i] == '.':
            number = ''

            while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                number += s[i]
                i += 1
            tokens.append(float(number))

        elif s[i:i + 2] == '==':
            tokens.append('==')
            i += 2
        elif s[i:i + 3] == 'pow':
            tokens.append('pow')
            i += 3
        elif s[i] in '+-*/(),':
            tokens.append(s[i])
            i += 1

    pos = 0

    def operand(): # смотрит знак / скобку / pow и пропускает
        nonlocal pos

        if tokens[pos] == '-':
            pos += 1
            return -operand()
        if tokens[pos] == '+':
            pos += 1
            return operand()
        if tokens[pos] == '(':
            pos += 1
            value = plus_minus()
            pos += 1  # пропускает )
            return value
        if tokens[pos] == 'pow':
            pos += 2  # пропускает pow и (
            x = plus_minus()
            pos += 1  # пропускает ,
            y = plus_minus()
            pos += 1  # пропускает )
            return x ** y
        if isinstance(tokens[pos], float):
            value = tokens[pos]
            pos += 1
            return value

    def multiplication_division(): # умножает, делит
        nonlocal pos
        value = operand()

        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right = operand()

            if op == '*':
                value *= right
            else:
                value /= right

        return value

    def plus_minus(): # складывает, минусует
        nonlocal pos
        value = multiplication_division()

        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right = multiplication_division()

            if op == '+':
                value += right
            else:
                value -= right

        return value

    result = plus_minus()

    if pos < len(tokens) and tokens[pos] == '==':
        pos += 1
        right = plus_minus()
        result = (result == right)

    return result

s = input("Введите выражение: ")
print("Результат:", calculate(s))