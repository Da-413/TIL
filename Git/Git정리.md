# 0711
## markdown
### 1. Heading
####### 여섯 개까지 사용 가능. 일곱 개부터는 지원하지 않음 \
 (notion은 세 개까지 지원)

table of content -> 목차를 생성하는 용도 \
이 때 Heading으로 구분되어 목차를 자동 생성

---
### 2. LIST

순서가 있는 리스트와 순서가 없는 리스트
1. 순서가
    1. 있는
2. 리스트\
 (리스트 구조화)

- 순서가
    - 없는
* 리스트
+ 혼용 가능(+, -, *)
    1. 순서가 있는 리스트, 순서가 없는 리스트 혼용 가능

---

### 3. code blck & inline code block

- 소스 코드를 붙여 넣을 때

print("Hello")

if (x > 10):
    print("x는 10보다 큽니다")

else:
    print("x는 10보다 작거나 같습니다")

------> 가독성 떨어지고 코드가 깨져 보일 수 있음

- code block

``` python
print("Hello")
if (x > 10):
    print("x는 10보다 큽니다")

else:
    print("x는 10보다 작거나 같습니다")
```

한 줄짜리 코드는?
--> 백틱(`)으로 감싸면 된다

`print("Hello World")`

(강조 기능)

---
### 4. 링크(link) & 이미지(image)

[텍스트 정보](링크)

[google](https://google.com)

[perplexity](http://perplexity.ai)

![이미지 대체 택스트](이미지 주소)

- 웹 상의 이미지

![lorem picsum](https://picsum.photos/300)

- 로컬 이미지

![local image](./img.jpg)

- 이미지의 크지 조정은 markdown에서 제공하지 않음

    - html의 image태그를 사용해서 조정 가능

<img src="./img.jpg" width = "100">

---

### 5. 텍스트 관련 문법

- 텍스트 **굵게**
- 텍스트 *기울기*
- 텍스트 ~~취소선~~

### 6. 인용 문구

> 인용 문구는 이렇게 표현 가능합니다
>> 인용의 인용 문구는 이렇게 표현 가능합니다

### 7. 표(table)

|First Header | Second Header|
| -----------: | :------------: |
|content      | content      |
|content       | content    |

:-- 좌측정렬

--: 우측정렬

:--: 가운데 정렬

### 8. 체크리스트

- [x] 체크리스트 1
- [x] 체크리스트 2
- [ ] 체크리스트 3

`vs코드에서는 지원을 안함`

##### 구글에 마크다운 치트시트 검색 ㄱㄱ

## CLI (Command Line Interface)

서버 관리에서는 자원을 서비스 제공에 최대한 이용하기 위해 CLI 환경 이용\
(효율성-키보드만으로 작동 + cpu사용 최소화, 정밀한 제어, 표준성)

현재 디렉토리 : .\
현재의 상위 디렉토리 : ..

### 기초 문법 (Bash)
1. touch : 파일 생성
```Bash
touch 파일이름.확장자
```
2. mkdir : 새 디렉토리 생성
```Bash
mkdir 폴더이름
```
3. ls : 현재 작업중인 디렉토리 안의 모든 파일 / 폴더
```Bash
ls
ls -a : 숨김 파일(폴더)까지 
```
 - 이름 뒤에 '/' 있으면 디렉토리(폴더)

`terminal에 나타난 text 초기화 : ctrl + L`

4. cd : 현재 위치 이동
```bash
cd 이동할 경로명
```
5. start : 파일 열기
```bash
start 파일/폴더명
(mac에서는 open 명령어 사용)
```
- code 명령어는 vscode에서 파일 실행

6. rm : 파일 삭제
```bash
rm 파일명
rm -r 디렉토리명
```
- -rf : 강제 삭제

7. mv : 현재 디렉토리의 파일 이동
```bash
mv '이동시킬 파일명' '이동시킬 디렉토리명'
```

## Git
- 분산 버전 관리 시스템

- 버전 관리 -> 변경 사항을 기록하고 저장하는 것
    -  변경 사항만 기록하고 있으면 자원을 아끼면서 모든 버전을 관리할 수 있음

- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리 <-> 중앙 집중식
    - 중앙 서버에 의존하지 않고도 동시에 작업을 진행할 수 있음 -> 개발자간 작업 충돌을 줄여주고 개발 효율성 향상
    - 중앙 서버 컴퓨터의 장애나 손실에 대비해 백업과 복구가 용이
    - 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음 -> 로컬에 기록 후 나중에 동기화

- git 은 프로그램 코드의 버전(변경사항)을 관리
---
### Git의 영역 (가상의 영역)

1. Working Directory
    - 실제 작업 중인 파일들이 위치하는 영역

2. Staging Area
    - working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
    - 실제 버전 관리할 파일을 선별하는 공간
3. Repository
    - 버전 이력과 파일들이 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨
    - 버전 이력 = commit = 변경된 파일들을 저장하는 행위
---
### Git 동작 순서

1. git init
    - 로컬 저장소 설정(초기화)
    - git의 버전 관리를 시작할 디렉토리에서 진행
    - 해당 폴더를 git으로 관리를 할 준비 / 보통 프로젝트 단위
    - (master) 표시 / .git폴더 생성(숨김 폴더)
2. git add
    - 변경 사항이 있는 파일을 working directory에서 staging area로 추가
    - git add . 은 현재 위치에 있는 모든 파일을 staging area에 추가
3. git commit
    - staging area에 있는 파일들을 저장소에 기록
    - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
    - ***commit -m 'message' : 협업에서 변경 내용을 기록해 줘야함***
    - commit 사용자와 e-mail 주인이 같으면 이력 저장(github)

```
git init : working directory 생성
-> git add : staging area로 파일 이동
-> git commint : repository로 변경 이력 저장
```
4. git log
    - commit된 내역을 볼 수 있음
    - git log --oneline : commit 내역을 한 줄로 볼 수 있음
5. git status
    - git의 현재 상태를 볼 수 있음

`untracked : 새 파일, working directory에만 있고 add되지 않은 상황`

`modified : 이미 commit되어 관리되고 있는 파일`

- '/' : root 폴더 (git bash에서는 program file의 git 폴더)
- '~' : home 폴더 (사용자 로그인된 폴더)
- git으로 관리되고 있는 폴더 내에서 git을 다시 설정하면 종속되면서 추가 설정이 필요해짐
    - 상위 폴더 확인 필요

- vim editor 모드 (insert가 맨 밑에 켜져있을 때)
    - message 작성
    - command 모드로 변경 (ESC키 누르기) -> insert 사라짐
    - :wq (저장하고 나가기), :q or :q! (저장하지 않고 나가기)
    - 다시 editor 모드로 변경 : i
---
### commit 수정하기
- 협업 시 함부로 수정하면 history가 바뀌면서 충돌이 발생할 수 있으니 주의 요망

- git commit --amend
    1. 직전에 생성한 commit 메세지 수정 
        - vim editor 상태에서 수정 가능
        - hash code가 바뀜 -> history가 바뀜

    2. 직전에 생성한 commit 전제 수정  
        - 수정할 파일을 staging area에 올린 후 amend 이용하여 최신 commit 수정

    3. commit을 버전 관리 측면에서 봤을 때 오타 수정, 파일 추가 등은 유효한 버전 변경 이라고 볼 수 없음 \
    따라서 꼭 유효한 버전만 관리하기 위해서 필요한 기능이라고 할 수 있다.










