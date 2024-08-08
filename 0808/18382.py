T = int(input())
for tc in range(1, T + 1):
    equation = list(input().split())

    numbers = []


    def calculate(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a // b

    flag = True
    for char in equation:
        if char.isdigit():
            numbers.append(int(char))
        elif char in ['+', '-', '*', '/']:
            if len(numbers) > 1:
                num2 = numbers.pop()
                num1 = numbers.pop()
                numbers.append(calculate(num1, num2, char))
            else:
                print(f'#{tc} error')
                flag = False
                break
        elif char == '.':
            if len(numbers) == 1:
                print(f'#{tc} {numbers[0]}')
            else:
                print(f'#{tc} error')
