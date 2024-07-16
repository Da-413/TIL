# 0712
## Remote Repository
- 원격 저장소 : 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간 <-> Local Repository
- ex\) github, gitlab, lab.ssafy => git을 이용하는 서비스

- `git remote add origin(별명) remote_repo_url(원격저장소 주소)` : 로컬 저장소에 원격 저장소 추가

- `git remote -v` : 현재 연결된 remote repository 확인
### Push
- 원격 저장소에 commit 파일이 올라가는 것
- `git push origin(별명) master(branch명)` : remote repository로 push
### Pull
- 최초 1회 : clone / 버전 정보가 있는 경우 : pull
    - push해도 버전 정보가 저장되므로 clone할 필요 없음

`git clone remote주소` : .git 폴더까지 복제됨 -> 버전 정보 관리 가능 / git init 필요 없음

### remote repository에 push하는 전체 과정
1. git pull remote주소
2. git add .
3. git commit -m 'message'
4. git push origin master

- 중간중간 status나 log로 관리 필요
- origin은 연결의 별명

### gitignore
`.gitignore 파일을 만든 뒤 파일 안에 black list 파일명을 등록`
- git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍트스 파일
- git add에서 추적하지 않도록 함
- 프로젝트에 따라 공유하지 않아야 하는 것들을 관리
- commit이 이루어지면 추적 대상에 등록됨 -> 추적 대상에 등록된 이후 gitignore에 등록해도 계속 추적됨 \
 -> git commit 이전에 gitignore에 등록해야함 -> git init 직후 등록 추천

```
gitignore.io
: Python, VScode 등의 파일에서 추적할 필요가 없는 파일들의 목록을 받아올 수 있음
git init -> .gitignore 생성 -> gitignore.io에서 목록 복사 후 .gitignore에 붙여넣기
```
### remote 삭제
`git remote rm origin(원격저장소 이름)` : 현재 로컬 저장소에 등록된 원격 저장소 삭제

## Git revert 와 Git reset

### Git revert
- 특정 commit을 없었던 일로 만드는 작업
- 이전 commit 내용을 없던 내용으로 한다는 새로운 커밋을 만든다
- 특정 시점의 commit 처리
- `git revert history` 이후 vim editor에서 새로운 commit 편집 후 종료
- history 기록을 유지하면서 새 commit을 만들기 때문에 기록의 무결성과 협업의 신뢰성을 높임
- 여러 개의 commit 동시에 revert 가능 : `git revert history1 history2 history3`
    - `git revert history1 .. history5` : 범위로 revert 가능
- vim editor 없이 commit하기 : `git revert --no-edit history`
- commit하지 않고 staging area에만 올림 : `git revert --no-commit history`

### Git reset
- 특정 commit으로 되돌아가는 작업
- `git reset [option] history`
- 특정 commit으로 되돌아 간 이후의 모든 commit은 삭제
- Option : 삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지
    1. --soft : 삭제된 commit의 기록을 staging area에 남김
    2. --mixed : 삭제된 기록을 working directory에 남김(기본 옵션)
    3. --hard : 삭제된 commit의 기록을 남기지 않음

### git reflog
- head가 이전에 가리켰던 모든 commit을 보여줌
- reset --hard 옵션으로 삭제된 commit도 확인할 수 있음

`git push -f` : 로컬에서 수정한 내용을 remote에도 적용시키기 위해 강제성이 필요
    
### Undoing
1. 파일 내용을 수정 전으로 되돌리기
    - `git restore` : Modified 상태의 파일 되돌리기
    - working directory에서 파일을 수정한 뒤 파일의 수정 사항을 취소하고 원래 모습대로 되돌리는 작업
    - 한 번이라도 commit에 등록된 파일만 가능
    - `git stash` : 작업한 내용을 다른 공간에 임시 저장하고 파일을 되돌림
    
    - `git stash apply` : 임시 저장한 작업 내용을 다시 불러옴

2. Staging Area에 올린 내용을 Unstage 하기
    - staging area에서 working directory로  

    1. `git rm --cached` : commit이 없는 경우 추적 대상에서 삭제
        - gitignore에 등록하기 위해 commit에서 제외시킬 때
        - 이미 commit 되어서 gitignore에 등록해도 계속 추적 대상일 때
        
    2. `git restore --staged` : commit이 존재하는 경우 추적 대상에서 삭제






































