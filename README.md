# TIL
## Git 카테고리

- [Git정리1](./Git/Git정리.md)
- [Git정리2](./Git/Git정리2.md)

[파이썬 수업자료](https://lab.ssafy.com/s12/python)

- d2coding 설치

    1. github에서 배포하는 1.3.2버전
    2. d2codingall 모든 사용자용으로 설치
    3. setting -> font family에서 d2coding
---

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

---

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

---

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

---

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

----

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

---   

### 0724 OOP(1) -Object Oriented Program

1. 객체 지향 프로그래밍

    - 절차 지향 프로그래밍 -> 객체 지향 프로그래밍

2. 클래스(Class)

    - 객체 : 속성(변수) + 행동(메서드)

    - 인스턴스 : 클래스로 만든 객체 (특정 클래스의 인스턴스)

        - ex) 문자열 타입의 변수는 str 클래스로 만든 인스턴스

        - 절차 지향 : 함수(데이터) -> 객체 지향 : 데이터.메서드()

    ```python
    class Person:         # Class 이름은 PascalCase로 
        pass

    iu = Person()           # 인스턴스 생성

    iu.method()             # 메서드 호출

    iu.attribute            # 속성 접근
    ```
             
3. 클래스 구조

    1. 생성자 메서드 : 객체를 생성할 때 자동으로 호출되는 특별한 메서드

        - __init__ 이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당 (__method__ : 매직 메서드)

        - 생성자 함수를 통해 인스턴스를 생성하고 초기값을 할당

    2. 인스턴스 변수 : 인스턴스마다 별도로 생성되는 변수
        
        - 인스턴스가 생성될 때마다 초기화 됨

    3. 클래스 변수 : 클래스 내부에 선언된 변수

        - 클래스로 생성된 모든 인스턴스들이 공유하는 변수

    4. 인스턴스 메서드 : 각각의 인스턴스 메서드에서 호출할 수 있는 메서드

        - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

    ```python
    class Person:
        blood_color = 'red'             # 클래스 변수

        def __init__(self, name):       # 생성자 메서드
            self.name = name            # 인스턴스 변수(name)

        def singing():                          # 인스턴스 메서드
            return f'{self.name}이 노래합니다.'
    ```

4. 메서드 종류

    1. 인스턴스 메서드

        - 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

        - 인스턴스의 상태를 조작하거나 동작을 수행

        - 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음

        ```python
        class MyClass:
            
            def instance_metho(self, arg1, ...):
                pass
        ```
        `'hello'.upper() 는 실제로 str.upper('hello') 처럼 작동 (단축형 호출) => self가 필요한 이유`

        - 생성자 메서드 < 인스턴스 메서드

    2. 클래스 메서드

        - @classmethod 데코레이터를 사용하여 정의

        - 호출시 첫 번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨

        ```python
        class MyClass:

            @classmethod
            def class_method(cls, arg1, ...):
                pass
        ```

    3. 스태틱 메서드

        - 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

        - 주로 클래스와 상호작용 하지만 인스턴스와 관련 없는 내용

        - 호출 시 필수적으로 작성해야 할 매개변수가 없음

        - 객체나 클래스 상태를 수정할 수 없으며 단지 기능한을 위한 메서드

        ```python
        class MyClass:

            @staticmethod
            def static_method():
                pass
        ```

    `클래스와 인스턴스 모두 클래스 메서드, 인스턴스 메서드 모두 호출할 수 있지만 각자의 역할에 맞는 메서드만 사용하도록 해야 함`

- 매직 메서드 : 특정 상황에서 자동으로 호출되는 메서드 < 인스턴스 메서드

    - ex) \_\_str\_\_ : 내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

- 데코레이터 : 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 __함수__

    
### 0725 OOP(2) - Object Oriented Program

1. 상속

    - 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

    - 상속이 필요한 이유
    
        1. 코드 재사용 : 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음, 중복된 코드를 줄일 수 있음

        2. 계층 구조 : 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음, 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

        3. 유지 보수 용이성 : 기존 클래스의 수정이 필요한 경우 부모 클래스만 수정하면 되므로 유지 보수가 용이해짐 -> 코드의 일관성을 유지하고 수정이 필요한 범위를 최소화할 수 있음

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age - age

        def talk(self):             # 메서드 재사용
            print(f'반갑습니다. {self.name}입니다.')

    class Professor(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

    p1 = Professor('박교수', 49, '컴퓨터공학과')
    s1 = Student('김학생', 20, 35)

    p1.talk() # 반갑습니다. 박교수입니다.
    s1.talk() # 반갑습니다. 김학생입니다.
    ```

2. 다중 상속

    - 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
    
    - 상속받은 모든 클래스의 요소를 활용 가능함

    - 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

    ```python
    class Person:
        def __init__(self, name):
            self.name = name

        def greeting(self):
            return f'안녕, {self.name}'

    class Mom(Person):
        gene = 'XX'

        def swin(self):
            return '엄마가 수영'

    class Dad(Person):
        gene = 'Xy'

        def walk(self):
            return '아빠가 걷기'

    class FirstChild(Dad, Mpm):
        def swim(self):
            return '첫째가 수영'

        def cry(self):
            return '첫째가 응애'

    baby1 = FirstChild('아가')

    print(baby1.cry())  # 첫째가 응애
    print(baby1.swim()) # 첫째가 수영
    print(baby1.walk()) # 아빠가 걷기
    print(baby1.gene)   # XY
    ```

    - 다이아몬드 문제

        - MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록 생성

        - 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음

        - 속성을 D -> B -> C 순서로 탐색
        `class D(B, C):`


    - super() : 부모 클래스 객체를 반환하는 내장 함수

        - 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

        ```python
        class ParentA:
            def __init__(self, arg):
                self.value_a = 'ParentA'

            def show_value(self):
                print(f'Value from ParentA: {self.value_a}')

        class ParentB:
            def __init__(self):
                self.value_b = 'ParentB'

            def show_value(self):
                print(f'Value from ParentB: {self.value_b}')
                
        class Child(ParentA, ParentB):
            def __init__(self):
                super().__init__(arg)  #ParantA 클래스의 __init__ 메서드 호출
                self.value_c = 'Child'

            def show_value(self):
                super().show_value()    # ParentA 클래스의 show_value 메서드 호출
                print(f'Value from Child: {self.value_c}')
        ```

    - mro() 메서드 : 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

        - 이름 공간을 인스턴스 -> 클래스 순으로 탐색에서 => 인스턴스 -> 자식 클래스 -> 부모 클래스 순으로 확장

    ```python
    class A:                    # 다이아몬드 구조
    def __init__(self):
        print('A Constructor')


    class B(A):
        def __init__(self):
            super().__init__()
            print('B Constructor')


    class C(A):
        def __init__(self):
            super().__init__()
            print('C Constructor')


    class D(B, C):
        def __init__(self):
            super().__init__()
            print('D Constructor')

    
    print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
    ```

    MRO가 필요한 이유

        - 부모 클래스들이 여러번 엑세스 되지 않도록 함

        - 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 구조 형성

        - 클래스의 신뢰성, 확장성 보장

        - 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용과 유지보수성이 향상

3. 에러와 예외

    - 문법 에러

        1. Invalid syntax (문법 오류)

        2. assign to literal (잘못된 할당)

        3. EOL (End of Line)

        4. EOF (End of File)

    - 예외 (Exception) : 프로그램 실행 중에 감지되는 에러

        - 내장 예외 : 예외 상황을 나타내는 예외 클래스들

        1. ZeroDivisionError

        2. NameError

        3. TypeError : 타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치

        4. ValueError

        5. IndexError

        6. KeyError

        7. ModuleNotFoundError

        8. ImportError

        9. KeyboardInterrupt

        10. IndentationError


4. 예외 처리

    - try ~ except ~ else ~ finally

    `주의 : 내장 예외는 클래스이므로 상속 관계가 있음 -> 예외 처리시 주의 필요`

















