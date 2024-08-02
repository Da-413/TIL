T = int(input())
for tc in range(1, T + 1):
    stick = input()
    stick = stick.replace('()', '1')

    save = []
    total = 0
    for par in stick:
        if par == '(' or par == '1':
            save.append(par)
        else:
            i = len(save) - 1
            cnt = 0
            while True:
                if save[i] == '1':
                    cnt += 1
                elif save[i] == '(':
                    total += (cnt + 1)
                    save.pop(i)
                    break
                i -= 1

    print(f'#{tc} {total}')
