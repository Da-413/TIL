import sys
sys.stdin = open('input.txt', 'r')

passowrd_dict = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
                  '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

def exchange(arr):
    length = len(arr)
    idx = length - 2
    password = ''
    cnt = 0
    while idx > 7 and cnt < 9:
        if arr[idx] == '1':
            candidate = ''
            for i in range(idx - 6, idx + 1):
                candidate = candidate + arr[i]
            password = password + passowrd_dict[candidate]
            idx -= 7
            cnt += 1
        else:
            idx -= 1
    password = ''.join(reversed(password))
    return password

def determine(password):
    result = 0
    for i in range(1, 9):
        if i % 2 == 0:
            result += int(password[i - 1])
        else:
            result += 3 * int(password[i - 1])
        
    return result


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        password = exchange(matrix[i])
        if password:
            if determine(password) % 10 == 0 and len(password) > 0:
                ans = sum(list(map(int, password)))
            break
    print(f'#{tc} {ans}')

