T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    adjl = [[] for _ in range(n + 1)]
    for i in range(1, n // 2 + 1):
        adjl[i].append(2 * i)
        if 2 * i + 1 <= n:
            adjl[i].append(2 * i + 1)

    value = [0] * (n + 1)
    num = 1


    def inorder(node):
        global num

        if adjl[node] == []:
            value[node] = num
            num += 1
            return
        
        inorder(adjl[node][0])
        value[node] = num
        num += 1
        if len(adjl[node]) == 2:
            inorder(adjl[node][1])

    inorder(1)
    print(f"#{tc} {value[1]} {value[n // 2]}")