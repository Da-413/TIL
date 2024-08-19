T = int(input())
for tc in range(1, T + 1):
    p = input()
    text = input()

    ans = 0

    for letter in p:
        cnt = 0
        for t in text:
            if letter == t:
                cnt += 1
        if cnt > ans:
            ans = cnt

    print(f'#{tc} {ans}')
