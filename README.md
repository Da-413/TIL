# TIL
## Git 카테고리

- [Git정리1](./Git/Git정리.md)
- [Git정리2](./Git/Git정리2.md)

[파이썬 수업자료](https://lab.ssafy.com/s12/python)

### 0716 - 기초 문법

1. tuple에 한 개의 값만을 저장할 때 주의할 점
    - a_tuple = (1,) : comma 없으면 정수형으로 인식

2. x, y = 10, 20 가능 (다중 할당)
    - 튜플은 comma로 생성 가능

3. 튜플은 불변 특성 / 내부 동작에 주로 사용됨

4. range 자료형은 list로 바꿔서 확인 가능
    - list(range(0,5)) => [0, 1, 2, 3, 4]

5. set
    - | : 합집합
    - \- : 차집합
    - & : 교집합

6. 변경 가능 : list dict set / 불가능 : str tuple
7. 순서 있음 : list str tuple / 없음 : dict set

8. 암시적 형변환 / 명시적 형변환
    - 암시적 형변환 : 파이썬이 자동으로 형변환
        - boolean과 numeric 타입에서만 가능
    - 명시적 형변환 : 프로그래머가 직접 지정하는 형변환

9. is / is not : 참조하는 메모리 주소까지 비교

10. 단축평가
    - and / or 연산자 앞에서 결론이 나면 뒤 조건은 평가하지 않음


### 0717 - 함수와 제어문(1)
1. 함수의 인자

    1. 위치 인자

    2. 기본 인자

    3. 키워드 인자

        - 키워드 인자는 위치 인자 뒤에 위치해야 함
    4. 가변 인자

        - \* : 튜플로 처리, ** : 딕셔너리로 처리

2. map & zip

    1. map(function, iterable)

    2. zip(*iterable)

3. 함수의 scope

    - local scope

    - global scope

    - LEGB rule : local -> enclosed -> global -> built-in 순서로 이름 검색

    ```python
    a = 1
    b = 2

    def enclosed():
        a = 10
        c = 3

        def local():
            print(a, b, c)   # 10 2 500

        local(500)
        print(a, b, c)  # 10 2 3

    enclosed()
    print(a, b)   # 1 2
    ```

4. packing & unpacking

    - \* : 패킹 연산자로 사용될 때 - 여러 개의 인자를 하난의 튜플로 묶음\
    언패킹 연산자로 사용될 때 - 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달

    - ** : 언패킹 연산자로 사용될 떄 - 딕셔너리의 키,값 쌍을 언패킹 하여 함수의 키워드로 전달

5. 람다 표현식

    `lambda 매개변수: 표현식`
    
    - ex) map 함수와 사용할 때
    ```python
    numbers = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
    ```

### 0718 - 함수와 제어문(2)
    
1. module

    - requests : pip install requests -> import requests\
        외부 API 접근하게 해주는 모듈
        
    - 직접 만들어서 사용 가능

2. 제어문

    1. 조건문
        - if ~ elif ~ else
        ```python
            if 표현식:
                코드블록
            elif 표현식:
                코드블록
            else:
                코드블록
        ```
    2. 반복문 
        - iterable(반복 가능)한 객체에 대해 적용
        - for
        ```python
            for 임시변수 in iterable객체:
                코드블록
        ```
        - while
        ```python
            while(조건식):
                코드블록
        ```

    3. 반복문 제어
        - break : 반복을 중지
        - continue : 다음 반복으로 건너 뜀
        - pass : 아무 동작을 수행하지 않고 넘어감

3. List comprehesion

    - `[x for x in range]`

    - 리스트를 생성하는 방법 

        1. for 반복문 .append : `for i in range(): [].append(i)`

        2. map : `list(map(lambda x: x, range()))`

        3. list comprehension : `[x for x in range()]`

* enumerate(iterable, start=0)\
: 인덱스와 값을 같이 하나의 튜플로 반환해주는 함수


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


### 0723 - Data Structure(2)

1. Dictionary

    1. dict.get(key) : 키에 연결된 값을 반환(없으면 none) 

    2. dict.keys() : 딕셔너리의 키를 모은 객체를 반환

    3. dict.values() : 딕셔너리의 값을 모은 객체를 반환

    4. dict.items() : 딕셔너리의 키,값 쌍을 모은 객체를 반환

    5. dict.pop(key) : 키를 제거하고 연결됐던 값을 반환(없으면 오류)

    6. dict.setdefault(key, value) : 키와 연결된 값을 반환 없으면 키, 값 쌍 추가

    7. dict.update(other) : other의 키,값 쌍으로 대체하거나 추가 

2. Set

    1. set.add(x) : x를 추가 

    2. set.remove(x) : x를 제거, 없으면 에러

    3. set.pop() : 임의의 항목을 반환하고 제거

    4. set.discard(x) : 항목 x를 제거

    5. set.update(iterable) : iterable 요소를 추가

    6. set1 - set2 / set1 & set2 / set1 | set2 / se1 <= set2

3. Hash Table

    - 해시 함수를 사용하여 변환한 값을 인덱스로 삼아 키와 데이터를 저장하는 구조

        -> 데이터 탐색이 매우 빠르게 이루어짐

    































