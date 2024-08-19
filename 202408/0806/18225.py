T = int(input())
for tc in range(1, T + 1):
    string = input()
    my_stack = []
    for char in string:
        if len(my_stack) == 0 or char != my_stack[-1]:
            my_stack.append(char)
        elif char == my_stack[-1]:
            my_stack.pop()
    print(f'#{tc} {len(my_stack)}')
