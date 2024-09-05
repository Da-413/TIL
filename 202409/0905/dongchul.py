def dfs(level):
    global n, prob, max_prob
    
    if level == n:
        if prob > max_prob:
            max_prob = prob
        return
    
    if prob <= max_prob:
        return
    
    for idx in range(n):
        if visited[idx] == 0:
            visited[idx] = 1
            temp = prob
            prob *= (work[level][idx] / 100)
            dfs(level + 1)
            visited[idx] = 0
            prob = temp
            




T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    max_prob = -1
    visited = [0] * n
    prob = 1
    dfs(0)

    ans = max_prob * 100
    print(f"#{tc} {ans:.6f}")