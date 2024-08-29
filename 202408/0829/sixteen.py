hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def transform(h):
    string = ['0', '0', '0', '0']
    idx = 3
    while h > 0:
        string[idx] = str(h % 2)
        h //= 2
        idx -= 1
    result = ''.join(string)
    return result

T = int(input())
for tc in range(1, T + 1):
    n, hex = input().split()
    hex = list(hex)
    lst = []
    for num in hex:
        if num.isdigit():
            lst.append(int(num))
        else:
            lst.append(hex_dict[num])
    result = list(map(transform, lst))
    ans = ''.join(result)
    print(f"#{tc} {ans}")
