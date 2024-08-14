import sys
sys.stdin = open('input.txt')

def bfs(s, v):
    visited = [[0] * v for _ in range(v)]
    ni, nj = s[0], s[1]
    queue = []
    queue.append(s)
    visited[ni][nj] = 1

    while queue:
        ti, tj = queue.pop(0)
        if maze[ti][tj] == '3':
            return 1

        for [di, dj] in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = ti + di
            nj = tj + dj
            if 0 <= ni < v and 0 <= nj < v and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1

    return 0


for tc in range(1, 11):
    t = int(input())
    maze = [list(input()) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                start = (i, j)

    print(f'#{tc} {bfs(start, 100)}')