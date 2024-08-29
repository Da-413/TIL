T = int(input().strip())

def transform(b):
    result = 0; i = 0
    while b > 0:
        result += (b % 10) * (2 ** i)
        b //= 10
        i += 1
    return result

for tc in range(1, T + 1):
    n = int(input().strip())
    input_list = []
    for _ in range(7):
        input_list.extend(list(input().strip()))
    binary_list = []
    for i in range(0, n * 10, 7):
        binary_list.append(''.join(input_list[i : i + 7]))
    target = list(map(int, binary_list))
    print(f'#{tc}', end=' ')
    for i in range(len(target)):
        print(transform(target[i]), end=' ')