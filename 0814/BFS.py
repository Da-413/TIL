v, e = map(int, input().split())
lst = list(map(int, input().split()))

adjL = [[] for _ in range(v + 1)]
for i in range(e):
    v1, v2 = lst[2 * i], lst[2 * i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)


def bfs(s, n):
    visited = [0] * (n + 1)
    queue = []
    visited[s] = 1
    queue.append(s)

    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for w in adjL[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1

print('#1', end=' ')
bfs(1, v)
