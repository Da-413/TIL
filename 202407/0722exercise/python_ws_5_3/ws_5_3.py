# 아래 함수를 수정하시오.
def sort_tuple(unsorted_tuple):
    new_tuple = ()
    length = len(unsorted_tuple)
    tuple_list = list(unsorted_tuple)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if tuple_list[j] > tuple_list[j + 1]:
                temp = tuple_list[j]
                tuple_list[j] = tuple_list[j + 1]
                tuple_list[j + 1] = temp
            
    new_tuple = tuple(tuple_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
