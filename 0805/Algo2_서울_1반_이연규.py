T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    climing = list(map(int, input().split()))                   # 등산로 리스트
    degree = []                                                 # 경사로 배열 초기화
    root = []                                                   # 경로별 경사로 저장할 배열 초기화

    for i in range(n - 1):

        if climing[i] <= climing[i + 1]:                            # 경사로 배열이 오름차순(다음에 나오는 값보다 작거나 같으면)이면 root에 추가
            root.append(climing[i])
        else:
            root.append(climing[i])                                 # 다음에 나오는 값이 작은 경우 그 값까지 root에 추가하고 경사로와 길이 계산 후 degree에 추가
            root_degree = (root[-1] - root[0]) / len(root)
            degree.append([root_degree, len(root)])
            root = []
        if i == n - 2:                                              # 마지막 전 인덱스인 경우 마지막 원소를 root에 추가한 뒤 마찬가지로 경사로와 길이 계산 후 degree에 추가
            root.append(climing[i + 1])
            root_degree = (root[-1] - root[0]) / len(root)
            degree.append([root_degree, len(root)])
            root = []
    if len(degree) == n:                                            # degree의 길이가 n인 경우 등산로 리스트가 내림차순으로 등산로가 없음을 의미 -> 0 출력
        print(0)
    else:                                                           # 그 외의 경우 경사로가 0인 root, 즉 등산로가 아닌 root는 삭제
        for lst in degree:
            if lst[0] == 0:
                degree.remove(lst)

        minimum = degree[0][0]; minimum_len = degree[0][1]          # 최소 경사로와 그 때의 길이를 초기화
        for i in range(len(degree)):
            if degree[i][0] < minimum:                              # 최소 경사로이면 길이를 최신화
                minimum_len = degree[i][1]
            elif degree[i][0] == minimum:                           # 경사로가 같다면 길이가 긴 경로의 길이로 최신화
                if degree[i][1] > minimum_len:
                    minimum_len = degree[i][1]

        print(f'#{tc} {minimum_len}')
