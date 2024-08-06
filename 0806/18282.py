T = int(input())


def check_pare(parenthesis):
    my_stack = []
    for par in parenthesis:
        if par == '(':
            my_stack.append(par)
        elif par == ')':
            if len(my_stack) == 0:
                return -1
            elif my_stack[-1] == '(':
                my_stack.pop()
            else:
                return -1
    if len(my_stack) != 0:
        return -1
    else:
        return 1


for tc in range(1, T + 1):
    pare = input().strip()
    print(f'#{tc} {check_pare(pare)}')
