import sys
sys.stdin = open('input.txt', 'r')

passowrd_dict = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
                  '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

def transform(password):
    length = len(password) // 56
    lst = []
    for i in range(0, len(password), 7 * length):
        word = password[i : i + 7 * length]
        temp = []
        for j in range(0, 7 * length, length):
            temp.append(word[j])
        temp = ''.join(temp)
        lst.append(passowrd_dict[temp])

    return ''.join(lst)

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
    n, m = map(int, input().strip().split())
    matrix = [input() for _ in range(n)]

    hex_password_list = []
    for word in matrix:
        password = '0x' + ''.join(word)
        hex_password_list.append(password)

    bin_password_list = []
    for word in hex_password_list:
        password = bin(int(word, 16))
        bin_password_list.append(password)

    password_list = []
    for bin_password in bin_password_list:
        if bin_password not in password_list:
            password_list.append(bin_password)
    password_list.remove('0b0')

    new_password = []
    for password in password_list:
        password = password.lstrip('0b')
        password = password.rstrip('0')
        new_password.append(password)

    

    ans = 0
    for password in new_password:
        trans = transform(password)
        result = determine(trans)
        if result % 10 == 0:
            ans += sum(list(map(int, trans)))
    print(f"#{tc} {ans}")