T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    prime = [2, 3, 5, 7, 11]
    ans = [0, 0, 0, 0, 0]

    for i in range(len(prime)):
        while n % prime[i] == 0:
            n //= prime[i]
            ans[i] += 1
        ans[i] = str(ans[i])

    print(f'#{tc} {" ".join(ans)}')