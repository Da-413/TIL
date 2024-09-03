def permutation(count):
    global max_value

    value = int(''.join(prize))
    if value in used[count]:
        return
    
    used[count].add(value)

    if count == time:
        if value > max_value:
            max_value = value
        return
    
    for i in range(len(prize) - 1):
        for j in range(i + 1, len(prize)):
            prize[i], prize[j] = prize[j], prize[i]
            permutation(count + 1)
            prize[i], prize[j] = prize[j], prize[i]


T = int(input())
for tc in range(1, T + 1):
    prize, time = input().split()
    time = int(time)
    prize = list(prize)
    max_value = 0
    used = [set() for _ in range(time + 1)]

    permutation(0)
    print(f"#{tc} {max_value}")