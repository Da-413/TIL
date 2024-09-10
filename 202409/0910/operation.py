from collections import deque

def bfs(num, target):
    queue = deque()
    visited[num] = 1
    queue.append(num)

    while queue:
        t = queue.popleft()
        dt = [t + 1, t - 1, t * 2, t - 10]
        for w in dt:
            if 0 < w <= 1000000 and visited[w] == 0:
                visited[w] = visited[t] + 1
                queue.append(w)
                if w == target:
                    return 



T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    
    bfs(n, m)
    print(f"#{tc} {visited[m] - 1}")