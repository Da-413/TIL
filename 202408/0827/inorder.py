import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(input().split()))

    adjL = [[] for _ in range(n + 1)]
    value = [0] * (n + 1)
    for i in range(n):
        if len(lst[i]) == 3:
            adjL[int(lst[i][0])].append(int(lst[i][2]))
        elif len(lst[i]) == 4:
            adjL[int(lst[i][0])].append(int(lst[i][2]))
            adjL[int(lst[i][0])].append(int(lst[i][3]))
        value[int(lst[i][0])] = lst[i][1]

    
    def inorder(node):
        if adjL[node] == []:
            print(value[node], end='')
            return
        
        inorder(adjL[node][0])
        print(value[node], end='')
        if len(adjL[node]) == 2:
            inorder(adjL[node][1])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()