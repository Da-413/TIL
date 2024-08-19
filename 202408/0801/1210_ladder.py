import sys
sys.stdin = open("input.txt", "r")

for i in range(10):
    tc = int(input())
    matrix = []
    target = 0
    for i in range(100):
        matrix.append(list(map(int, input().split())))

    for i in range(100):
        if matrix[-1][i] == 2:
            target = i
            break

    for i in range(99, -1, -1):
        while target < 99 and matrix[i][target + 1] == 1:
            matrix[i][target] = 2
            target += 1
        
        while 0<= target and matrix[i][target - 1] == 1:
            matrix[i][target] = 2
            target -= 1

    print(f'#{tc} {target}')