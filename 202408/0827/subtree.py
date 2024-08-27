T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    M = max(arr)
    adjl = [[] for _ in range(M + 1)]
    for i in range(e):
        v1, v2 = arr[2 * i], arr[2 * i + 1]
        adjl[v1].append(v2)

    cnt = 0
    

    def preorder(node):
        global cnt
        if adjl[node] == []:
            cnt += 1
            return
        
        cnt += 1

        preorder(adjl[node][0])
        if len(adjl[node]) == 2:
            preorder(adjl[node][1])


    preorder(n)
    print(f"#{tc} {cnt}")