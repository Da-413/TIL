T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    lst = []
    for i in range(e):
        lst.extend(list(map(int, input().split())))
    start, end = map(int, input().split())
    adjL = [[] for _ in range(v + 1)]
    for i in range(e):
        v1, v2 = lst[2*i], lst[2*i + 1]
        adjL[v1].append(v2)


    def DFS(s, n):
        stack = []
        visited = [0] * (n + 1)
        v = s
        visited[s] = 1

        while True:
            for w in adjL[v]:
                if not visited[w]:
                    stack.append(v)
                    visited[w] = 1
                    v = w
                    break
            else:
                if stack:
                    v = stack.pop()
                else:
                    break

        return visited


    result = DFS(start, v)
    print(f'#{tc} {result[end]}')
