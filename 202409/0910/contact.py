import sys
sys.stdin = open('input.txt')

def bfs(s):
    queue = []
    visited[s] = 1
    queue.append(s)

    while queue:
        t = queue.pop(0)
        for w in adjl[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1


for tc in range(1, 11):
    e, s = map(int, input().split())
    lst = list(map(int, input().split()))
    adjl = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, e, 2):
        v1, v2 = lst[i], lst[i + 1]
        adjl[v1].append(v2)

    bfs(s)
    M = max(visited)
    ans = 0
    for i in range(len(visited) - 1, -1, -1):
        if visited[i] == M:
            ans = i
            break

    print(f"#{tc} {ans}")