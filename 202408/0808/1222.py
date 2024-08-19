import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    lst = list(input())
    numbers = []
    stack = []

    for char in lst:
        if char.isdigit():
            numbers.append(int(char))
        else:
            stack.append(char)

    while len(numbers) > 1:
        num2 = numbers.pop()
        num1 = numbers.pop()
        if stack:
            numbers.append(num1 + num2)
            stack.pop()

    print(f'#{tc} {numbers[0]}')