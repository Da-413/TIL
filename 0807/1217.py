for _ in range(10):
    tc, n = map(int, input().split())
    lst = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(n):
        v1 = lst[2 * i]; v2 = lst[2*i + 1]
        adj_list[v1].append(v2)


    def DFS(s, M):
        stack = []
        visited = [0] * M
        v = s
        while True:
            for w in adj_list[v]:
                if not visited[w]:
                    stack.append(v)
                    v = w
                    visited[w] = 1
                    break
            else:
                if stack:
                    v = stack.pop()
                else:
                    break
        return visited


    result = DFS(0, 100)

    if result[-1] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')