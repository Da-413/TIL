# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    list1 = list(set1)
    list2 = list(set2)

    for e in list2:
        if e not in list1:
            list1.append(e)

    return set(list1)

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
