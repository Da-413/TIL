def run_or_triplet(arr):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                lst = [arr[i], arr[j], arr[k]]
                lst.sort()
                if arr[i] == arr[j] == arr[k]:
                    return True
                if lst[0] + 2 == lst[1] + 1 == lst[2]:
                    return True
                

T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    a = []; b = []
    winner = 0
    for i in range(0, len(card) - 1, 2):
        a.append(card[i])
        b.append(card[i + 1])
        
        if i >= 4:
            if run_or_triplet(a):
                winner = 1
                break
            if run_or_triplet(b):
                winner = 2
                break

    print(f"#{tc} {winner}")