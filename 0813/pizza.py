T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    for idx, value in enumerate(cheese):
        cheese[idx] = [value, idx]

    my_queue = []
    for i in range(n):
        i = i
        my_queue.append(cheese[i])
    i += 1

    while True:
        for j in range(len(my_queue)):
            my_queue[j][0] //= 2

        front = 0
        while front < len(my_queue):
            if my_queue[front][0] == 0:
                my_queue.pop(front)
                front -= 1
                if i < m:
                    my_queue.insert(front + 1, cheese[i])
                    i += 1
            if len(my_queue) == 1:
                break
            front += 1

        if len(my_queue) == 1:
            print(f'#{tc} {my_queue[0][1] + 1}')
            break