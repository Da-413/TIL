# 아래 함수를 수정하시오.
def count_character(string, char):
    result = 0
    for s in string:
        if s == char:
            result += 1
    return result


result = count_character("Hello, World!", "o")
print(result)  # 2
