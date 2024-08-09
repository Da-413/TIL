def calculator(a, b, operand):
    if operand == '+':
        return a + b
    elif operand == '*':
        return a * b


for tc in range(1, 11):
    n = int(input())
    calculate = list(input())
    result = []
    stack = []

    for char in calculate:
        if char.isdigit():
            result.append(int(char))
        elif char == '*':
            stack.append(char)
        else:
            if not stack or stack[-1] == '+':
                stack.append(char)
            else:
                while stack:
                    num2 = result.pop()
                    num1 = result.pop()
                    op = stack.pop()
                    result.append(calculator(num1, num2, op))
                stack.append(char)

    while stack:
        num2 = result.pop()
        num1 = result.pop()
        op = stack.pop()
        result.append(calculator(num1, num2, op))

    print(f'#{tc} {result[0]}')
