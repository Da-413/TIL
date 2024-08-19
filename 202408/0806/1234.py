for tc in range(1, 11):
    n, password = input().split()
    n = int(n)

    def check_password(password):
        my_stack = []
        for word in password:
            if len(my_stack) == 0 or my_stack[-1] != word:
                my_stack.append(word)
            elif my_stack[-1] == word:
                my_stack.pop()
        return my_stack

    ans = ''.join(check_password(password))
    print(f'#{tc} {ans}')