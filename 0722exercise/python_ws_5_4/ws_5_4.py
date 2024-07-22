# 아래 함수를 수정하시오.
def capitalize_words(string):
    
    title_str = []

    for s in string.split(' '):
        title_str.append(s.capitalize())

    return ' '.join(title_str)

result = capitalize_words("hello, world!")
print(result)
