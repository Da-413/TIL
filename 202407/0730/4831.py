T = int(input())
for tc in range(1, T + 1): 
    k, n, m = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    starting = 0
    move = 0

    while starting + k < n:
        
        for i in range(k, 0, -1):
            
            if (starting + i) in bus_stop:

                starting += i
                move += 1    
                break
                
        else:
            move = 0
            break
                

    print(f'#{tc} {move}')