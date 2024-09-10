def dfs(s):
    global cnt

    stack = []
    visited[s] = 1
    v = s
    
    while True:
        for w in adjl[v]:
            if visited[w] == 0:
                stack.append(v)
                visited[w] = 1
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
    v, e = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [0] * (v + 1)
    adjl = [[] for _ in range(v + 1)]
    for i in range(e):
        v1, v2 = lst[2 * i], lst[2 * i + 1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)
    
    cnt = 0
    for i in range(1, v + 1):
        if visited[i] == 0:
            dfs(i)

    print(f"#{tc} {cnt}")