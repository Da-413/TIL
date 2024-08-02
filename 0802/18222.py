T = int(input())
for tc in range(1, T + 1):
    word = input().strip()

    def find_palin(word):
        if len(word) == 0 or len(word) == 1:
            return 1
        else:
            if word[0] != word[-1]:
                return 0
            else:
                word = word[1:-1]
                return find_palin(word)

    print(f'#{tc} {find_palin(word)}')