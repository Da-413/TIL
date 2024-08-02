T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    l1 = len(str1); l2 = len(str2)
    ans = 0
    for i in range(l2 - l1 + 1):
        if str1 == str2[i:i + l1]:
            ans = 1

    print(f'#{tc} {ans}')