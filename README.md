# TIL
## Git 카테고리

- [Git정리1](./Git/Git정리.md)
- [Git정리2](./Git/Git정리2.md)

[파이썬 수업자료](https://lab.ssafy.com/s12/python)

### 0716
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


### 0717
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
        언패킹 연삱로 사용될 때 - 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달

        - ** : 언패킹 연산자로 사용될 떄 - 딕셔너리의 키,값 쌍을 언패킹 하여 함수의 키워드로 전달

    5. 람다 표현식

    `lambda 매개변수: 표현식`
    
    - ex) map 함수와 사용할 때
    ```python
    numbers = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
    ```