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