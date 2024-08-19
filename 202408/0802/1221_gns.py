import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    *num, n = input().split()
    n = int(n)
    lst = list(input().split())
    gns_dict = {"ZRO": '0', "ONE": '1', "TWO": '2', "THR": '3', "FOR": '4', "FIV": '5',
                "SIX": '6', "SVN": '7', "EGT": '8', "NIN": '9'}

    for i in range(n):
        lst[i] = gns_dict[lst[i]]

    for i in range(n - 2):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    rev_gns_dict = dict(zip(list(gns_dict.values()), list(gns_dict.keys())))

    for i in range(n):
        lst[i] = rev_gns_dict[lst[i]]
    print(f'#{tc}')
    print(*lst)

