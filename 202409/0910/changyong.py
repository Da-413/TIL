def dfs(s):
    global cnt

    stack = []
    visited[s] = 1
    v = s

    while True:
        for w in adjl[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                cnt += 1
                break

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    visited = [0] * (n + 1)
    adjl = [[] for _ in range(n + 1)]
    for i in range(m):
        temp = arr[i]
        v1, v2 = temp[0], temp[1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)
    
    cnt = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
    
    print(f"#{tc} {cnt}")
