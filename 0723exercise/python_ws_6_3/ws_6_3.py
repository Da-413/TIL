# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    list1 = list(set1)
    list2 = list(set2)
    intersection = []

    for e in list1:
        if e in list2:
            intersection.append(e)

    return set(intersection)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)
