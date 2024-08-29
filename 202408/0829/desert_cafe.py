T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    desert_list = []
    for i in range(n):
        for j in range(n):
            desert = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                while 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    desert.append(cafe[nx][ny])
                    nx += dx[k]
                    ny += dy[k]
                if nx == i and ny == j:
                    
            desert_list.append(desert)
    
    ans_list = []
    for i in range(len(desert_list)):
        if len(set(desert_list[i])) == len(desert_list[i]):
            ans_list.append(desert_list[i])

    print(ans_list)