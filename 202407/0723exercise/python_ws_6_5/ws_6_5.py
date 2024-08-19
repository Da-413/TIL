# 아래 함수를 수정하시오.
def difference_sets(set1, set2):
    list1 = list(set1)
    list2 = list(set2)

    for e in list2:
        if e in list1:
            list1.remove(e)

    return set(list1)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
