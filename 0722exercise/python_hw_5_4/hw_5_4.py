# 아래 함수를 수정하시오.
def find_min_max(lst):
    m = M = lst[0]
    for e in lst:
        if e < m:
            m = e
        if e > M:
            M = e
    return m, M


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
