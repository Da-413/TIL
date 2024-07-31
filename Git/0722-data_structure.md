### 0722 - Data Structure(1)

1. 메서드(method)\
: 객체에 속한 함수 (객체 = class), 각 객체마다 다양한 기능을 가진 method가 존재\
`데이터 타입 객체.메서드()   : 'hello'.capitalize()  # Hello`

2. 문자열 메서드 -> 새 문자열 반환 (문자열은 수정할 수 없는 자료형)

    1. s.replace(old, new[count]; 대괄호는 선택인자) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

    2. s.strip([chars]) : 공백이나 특정 문자를 제거

    3. s.split(sep=None, maxsplit=-1) : 공백이나 특정 문자를 기준으로 분리
    
    4. s.join(iterable) : 구분자(s)로 iterable의 문자열을 연결한 문자열을 반환

    5. capitalize(), title(), upper(), lower(), swapcase()

3. list method -> 리스트 원본을 변경

    1. l.append(x) : 리스트 마지막에 항목 추가

    2. l.extend(m) : iterable한 m의 모든 항목을 리스트 끝에 추가
 
    3. l.insert(i, x) : 원하는 위치에 항목 추가

    4. l.remove(x) : 처음 등장하는 x 제거

    5. l.pop([index]) : 리스트 마지막 요소 제거하고 반환

    6. l.index(x) : 첫 번째 x의 인덱스 반환

    7. l.count(x) : x의 개수 반환

    8. l.reverse() : 리스트 역배열

    9. l.sort(reverse = False) : 리스트 정렬 (오름차순)

4. 복사()

    - 변경 가능한 데이터 타입과 변경 불가능한 데이터 타입에서 복사가 다르게 작동

    1. 할당 => 복사 x, 두 객체가 같은 주소를 가리키게 됨 (객체의 참조를 복사)

    ```python
    a = [1, 2, 3, 4]
    b = a
    b[0] = 100

    print(a)  # [100, 2, 3, 4]
    print(b)  # [100, 2, 3, 4]


    a = 20
    b = a
    b = 10    # a=20 이후에 a=10을 재할당하면 a는 다른 주소의 10을 가리키게 됨
              # 같은 원리로 b도 다른 주소의 10을 가리키게 됨

    print(a)  # 20
    print(b)  # 10
    ```
    
    - 가변 데이터와 불변 데이터에서 작동이 다름

    2. 얕은 복사

    ```python
    a = [1, 2, 3, 4]
    b = a[:]     # 같은 값이지만 다른 주소를 가리키게 됨
    c = a.copy()     # .copy()는 슬라이싱과 같은 동작

    b[0] = 100
    c[0] = 99

    print(a)    # [1, 2, 3, 4]
    print(b)    # [100, 2, 3, 4]
    print(c)    # [99, 2, 3, 4]
    ```
    - 얕은 복사의 한계 : 중첩된 리스트를 복사하지 못하고 할당하게 됨

    ```python
    a = [1, 2, [3, 4, 5]]   # a의 2번 인덱스는 [3,4,5] 리스트의 주소를 가리키고 있음
    b = [:]

    b[2][0] = 100

    print(a)    # [1, 2, [100, 4, 5]]
    print(b)    # [1, 2, [100, 4, 5]]
    ```

    3. 깊은 복사

    ```python
    import copy

    a = [1, 2, [3, 4, 5]]
    b = copy.deepcopy(a)

    b[2][0] = 100

    print(a)    # [1, 2, [3, 4, 5]]
    print(b)    # [1, 2, [100, 4, 5]]
    ```