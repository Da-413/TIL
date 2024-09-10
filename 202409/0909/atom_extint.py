T = int(input())

dy = [0.5, -0.5, 0, 0]
dx = [0, 0, -0.5, 0.5]
for tc in range(1, T + 1):
    n = int(input())
    info = []
    for _ in range(n):
        info.append(list(map(int, input().split())))

    energy = 0
    while True:
        value = {}
        for i in range(len(info)):
            info[i][0] += dx[info[i][2]]
            info[i][1] += dy[info[i][2]]
            if value.get((info[i][0], info[i][1]), False):
                value[(info[i][0], info[i][1])] += 1
            else:
                value[(info[i][0], info[i][1])] = 1
        print(value)

        

        if info[i][0] > 1000 or info[i][0] < -1000 or info[i][1] > 1000 or info[i][1] < -1000:
            break


    # print(f"#{tc} {energy}")