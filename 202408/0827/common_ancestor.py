T = int(input())
for tc in range(1, T + 1):
    v, e, node1, node2 = map(int, input().split())
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(v + 1)]
    for i in range(e):
        parent, child = arr[2 * i], arr[2 * i + 1]
        adjl[parent].append(child)
    

    def preorder(node):
        global cnt, check

        if node == node1:
            check += 1
        if node == node2:
            check += 1

        if adjl[node] == []:
            cnt += 1
            return
        
        cnt += 1

        preorder(adjl[node][0])
        if len(adjl[node]) == 2:
            preorder(adjl[node][1])

    
    ans_lst = []
    for k in range(v):
        cnt = 0
        check = 0
        preorder(k)
        if check == 2:
            ans_lst.append([k, cnt])

    ans = ans_lst[0][1]; ancestor = ans_lst[0][0]
    for lst in ans_lst:
        if lst[1] < ans:
            ans = lst[1]
            ancestor = lst[0]

    print(f"#{tc} {ancestor} {ans}")