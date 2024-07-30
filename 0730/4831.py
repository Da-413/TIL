k, n, m = map(int, input().split())
bus_stop = list(map(int, input().split()))

starting = -1
move = 0

while starting < n:
    if starting + k >= n:
        move += 1
        break

    for i in range(k, 0, -1):

        if (starting + i) in bus_stop:
            starting += i
            move += 1
        else:
            move = 0
            break
    
    if move == 0:
        break
    
print(move)