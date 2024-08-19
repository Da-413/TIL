# 아래 함수를 수정하시오.
def even_elements(all_list):
    even_list = []

    for i in range(1, len(all_list), 2):
        even_list.extend(all_list[i-1:i+1])
        even_list.pop((i - 1) // 2)

    return even_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
