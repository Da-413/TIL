import sys
sys.stdin = open('input.txt')


def cal(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x +-y
    if op == '*':
        return x * y
    if op == '/':
        return int(x / y)

for tc in range(1, 11):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]

    value = [0] * (n + 1)
    adjL = [[] for _ in range(n + 1)]
    for lst in arr:
        if lst[1] in ['+', '-', '*', '/']:
            value[int(lst[0])] = lst[1]
            adjL[int(lst[0])].append(int(lst[2]))
            adjL[int(lst[0])].append(int(lst[3]))
            
        else:
            value[int(lst[0])] = int(lst[1])

    stack = []
    def postorder(node):
        if not adjL[node]:
            stack.append(value[node])
            return
        
        postorder(adjL[node][0])
        postorder(adjL[node][1])
        stack.append(value[node])
        

    postorder(1)
    stack = stack[::-1]
    result = []
    while stack:
        q = stack.pop()
        if type(q) == int:
            result.append(q)
        else:
            y = result.pop()
            x = result.pop()
            result.append(cal(x, y, q))

    print(f"#{tc} {result[0]}")