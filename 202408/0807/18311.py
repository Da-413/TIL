v, e = map(int, input().split())
lst = list(map(int, input().split()))
adjL = [[] for _ in range(v + 1)]
for i in range(e):
    v1, v2 = lst[2*i], lst[2*i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)


def DFS(s, n):
    stack = []
    visited = [0] * (n + 1)
    visited[s] = 1
    print(s, end='')
    v = s
    while True:
        for w in adjL[v]:
            if not visited[w]:
                stack.append(v)
                visited[w] = 1
                print(f'-{w}', end='')
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


print('#1', end=' ')
DFS(1, v)
