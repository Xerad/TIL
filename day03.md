# 3일차 TIL

## [1] Branch

> Git에서 Branch라는 개념은 매우 중요합니다. 사실상 버전 관리의 꽃이라고 할 수 있습니다.

### (1) Branch란?

- Branch는 `나뭇가지`라는 뜻의 영어 단어입니다.
- 즉 `브랜치`란 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 **독립적으로 작업**할 수 있도록 도와주는 Git의 도구입니다.
- 장점
  1. 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전합니다.
  2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능합니다.
  3. 특히나 Git은 브랜치를 만드는 속도가 굉장히 빠르고, 용량도 적게 듭니다.
- 그래도 브랜치 꼭 써야하나요?
  1. 일단 master 브랜치는 상용을 의미합니다. 그래서 언제든 세상에 공개되어 있습니다.
  2. 만약 상용에 에러가 있어서 고쳐야 한다면 어떻게 해야할까요?
  3. 고객들이 사용하고 있는데, 함부로 버전을 되돌리거나 삭제할 수 있을까요?
  4. 따라서 브랜치를 통해 별도의 작업 공간을 만들고, 그곳에서 되돌리거나 삭제를 합니다.
  5. 브랜치는 완전하게 독립이 되어있어서 어떤 작업을 해도 master에는 영향을 끼치지 못하죠.
  6. 그리고 이후에 에러를 해결했다면? 그 내용을 master에 반영할 수도 있습니다!
  7. 이러한 이유 때문에 Git에서 브랜치는 정말 강력한 기능 중의 하나라고 할 수 있습니다.

### (2) git branch

> 브랜치 `조회, 생성, 삭제 등` 브랜치와 관련된 Git 명령어

```bash
# 브랜치 목록 확인
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 새로운 브랜치 생성
$ git branch <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성
$ git branch <브랜치 이름> <커밋 ID>

# 특정 브랜치 삭제
$ git branch -d <브랜치 이름> # 병합된 브랜치만 삭제 가능
$ git branch -D <브랜치 이름> # (주의) 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
```

### (3) git switch

> 현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어 `HEAD`란 현재 브랜치를 가리키는 포인터를 의미합니다.

```bash
# 다른 브랜치로 이동
$ git switch <다른 브랜치 이름>

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성과 동시에 이동
$ git switch -c <브랜치 이름> <커밋 ID>
```

<aside> ❗ 잠깐! **git switch 하기 전에, 워킹 디렉토리 파일이 모두 버전 관리가 되고 있나요?**

master 브랜치와 feature 브랜치가 있다고 가정해보겠습니다. feature 브랜치에서 test.txt를 만들고 git add 하지 않은 상태에서 `git switch master`를 하면 어떤 일이 발생할까요? 바로 feature 브랜치에서 만들었던 test.txt가 master 브랜치에도 똑같이 생성됩니다.

**왜 그럴까요?** Git의 브랜치는 독립적인 작업 공간을 가지지만, 어디까지나 Git이 관리하는 파일 트리에 한해서 입니다. git add를 하지 않은, 즉 Staging Area에 한 번도 올라가지 않은 새 파일은 Git의 버전 관리를 받고 있지 않기 때문에 브랜치가 바뀌더라도 계속 유지되는 것입니다.

따라서 반드시 git switch를 하기 전에는 모든 워킹 디렉토리의 파일이 버전 관리가 되고 있는지 확인해야 합니다.

</aside>

## [2] Branch scenario

> git branch와 git switch를 통해 브랜치를 `조회, 생성, 이동`하는 실습을 진행합니다.

### (1) 사전 세팅

1. 홈 디렉토리에 `git-branch-practice` 폴더를 생성하고 이동 후 vscode를 엽니다.

   ```bash
   $ mkdir git-branch-practice
   $ cd git-branch-practice
   $ code .
   ```

2. Git 저장소를 생성합니다.

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/kyle/git-branch-practice/.git/
   ```

3. `test.txt`를 생성하고 각각 `master-1, master-2, master-3` 이라는 내용을 순서대로 입력하여 커밋 3개를 작성합니다.

   ```bash
   $ touch test.txt
   
   test.txt에 master-1 작성
   $ git add .
   $ git commit -m "master-1"
   
   test.txt에 master-2 작성
   $ git add .
   $ git commit -m "master-2"
   
   test.txt에 master-3 작성
   $ git add .
   $ git commit -m "master-3"
   ```

4. `git log --oneline`을 입력했을 때 아래와 같이 나와야 정상입니다.

   총 3개의 버전이 master 브랜치에 만들어졌습니다.

   ```bash
   $ git log --oneline
   0604dcd (HEAD -> master) master-3
   9c22c89 master-2
   3d71510 master-1
   ```

### (2) 브랜치 생성, 조회

1. 현재 위치(master 브랜치의 최신 커밋)에서 `login`이라는 이름으로 브랜치를 생성합니다.

   ```bash
   $ git branch login
   ```

2. login브랜치가 잘 생성되었는지 확인합니다.

   `* master`의 의미는 현재 HEAD가 가리키는 브랜치는 `master`라는 것입니다.

   ```bash
   $ git branch
   	login
   * master
   ```

3. `git log --oneline`을 입력했을 때 아래와 같이 나와야 정상입니다.

   `0604dcd` 커밋 기준으로 `master`와 `login`브랜치가 위치한 것을 볼 수 있습니다.

   ```bash
   $ git log --oneline
   0604dcd (HEAD -> master, login) master-3
   9c22c89 master-2
   3d71510 master-1
   ```

4. `master` 브랜치에서 1개의 커밋을 더 작성합니다.

   ```bash
   test.txt에 master-4 작성
   $ git add .
   $ git commit -m "master-4"
   ```

### (3) 브랜치 이동

1. 현재 브랜치와 커밋의 상태는 다음과 같습니다.

   ```bash
   $ git log --oneline
   5ca7701 (HEAD -> master) master-4
   0604dcd (login) master-3
   9c22c89 master-2
   3d71510 master-1
   ```

2. 이때 `login`브랜치로 이동하면 어떤 일이 일어날까요?

   ```bash
   $ git switch login
   ```

   **master 브랜치의 test.txt에 작성한 master-4가 지워졌습니다!!**

   ```bash
   # login 브랜치의 test.txt
   
   master-1
   master-2
   master-3
   ```

3. 그리고 `git log --oneline`을 입력하면 아래와 같이 나타납니다.

   이제 `HEAD`는 `login` 브랜치를 가리키고, `master` 브랜치가 보이지 않습니다.

   ```bash
   $ git log --oneline
   0604dcd (HEAD -> login) master-3
   9c22c89 master-2
   3d71510 master-1
   ```

4. master 브랜치는 삭제된 걸까요?

   아닙니다! 브랜치를 조회 해보면 다음과 같이 나타납니다.

   HEAD가 `login` 브랜치를 가리키면서, log도 `login` 브랜치 기준으로 보이는 것이었습니다.

   ```bash
   $ git branch
   * login
     master
   ```

5. `git log --oneline --all`을 입력하면 모든 브랜치의 로그를 볼 수 있습니다.

   ```bash
   $ git log --oneline --all
   5ca7701 (master) master-4
   0604dcd (HEAD -> login) master-3
   9c22c89 master-2
   3d71510 master-1
   ```



💡 즉 브랜치를 이동한다는건 HEAD가 해당 브랜치를 가리킨다는 것을 의미하고 브랜치는 최신 커밋을 가리키므로, **HEAD가 해당 브랜치의 최신 커밋을 가리키게 됩니다.

따라서 워킹 디렉토리의 내용도 HEAD가 가리키는 브랜치의 최신 커밋 상태로 변화합니다.**

### (4) login 브랜치에서 커밋 생성

1. `test.txt` 파일에 `login-1`이라고 작성합니다.

   ```bash
   # login 브랜치의 test.txt
   master-1
   master-2
   master-3
   login-1
   ```

2. 추가적으로 `test_login.txt`도 생성하고 `login-1`이라고 작성해봅시다.

   ```bash
   $ touch test_login.txt
   
   # 이후 test_login.txt에 작성
   login-1
   ```

3. 커밋을 생성합니다.

   ```bash
   $ git add .
   $ git commit -m "login-1"
   ```

4. `git log --oneline --all --graph`를 통해 아래와 같은 내용을 확인합니다.

   `master` 브랜치와 `login` 브랜치가 다른 갈래로 갈라진 것을 확인할 수 있습니다.

   ```bash
   $ git log --oneline --graph --all
   * 3b0a091 (HEAD -> login) login-1
   | * 5ca7701 (master) master-4
   |/
   * 0604dcd master-3
   * 9c22c89 master-2
   * 3d71510 master-1
   ```

---

## [1] Branch Merge

> 지금까지는 브랜치를 통해서 독립된 작업 공간을 만드는 것 까지 진행했습니다. 이제 각 브랜치에서의 작업이 끝나면 어떻게 할까요? 그 작업 내용을 master에 반영해야 하지 않을까요? 지금부터는 `Merge`라고 하는 `병합`을 학습하면서 브랜치를 합치는 것을 살펴보겠습니다.

### (1) git merge

- 분기된 브랜치들을 하나로 합치는 명령어

- `git merge <합칠 브랜치 이름>`의 형태로 사용합니다.

- **Merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야합니다.**

  ```bash
  # 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 입니다.
  $ git branch
  * branch1
    branch2
  
  # 2. branch2를 branch1에 합치려면?
  $ git merge branch2
  
  # 3. branch1을 branch2에 합치려면?
  $ git switch branch2
  $ git merge branch1
  ```

### (2) Merge의 세 종류

1. Fast-Forward

   - 브랜치를 병합할 때 마치 `빨리감기`처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것

   1. 현재 master는 C2 커밋을, hotfix는 C4 커밋을 가리키고 있습니다.

      ![image-20220225172435870](3일차강의자료.assets/image-20220225172435870.png)

   2. master에 hotfix를 병합하면 어떻게 될까요?

      ```bash
      $ git switch master
      $ git merge hotfix
      Updating s1d5f1s..1325sd4
      **Fast-forward**
       index.html | 2 ++
       1 file changed, 2 insertions(+)
      ```

   3. hotfix가 가리키는 C4는 C2에 기반한 커밋이므로, master가 C4에 이동하게 됩니다.

      이렇게 따로 merge 과정 없이 브랜치의 포인터가 이동하는 것을 `Fast-Forward`라고 합니다.

      ![image-20220225172450393](3일차강의자료.assets/image-20220225172450393-16457774919341.png)

   4. 병합이 완료된 hotfix는 더 이상 필요 없으므로 삭제합니다.

      ```bash
      $ git branch -d hotfix
      Deleted branch hotfix (1325sd4).
      ```

2. 3-Way Merge

- 브랜치를 병합할 때 `각 브랜치의 커밋 두개와 공통 조상 하나`를 사용하여 병합하는 것
- 두 브랜치에서 `다른 파일` 혹은 `같은 파일의 다른 부분`을 수정했을 때 가능합니다.

1. 현재 master는 C4 커밋을, iss53은 C5 커밋을 가리키고 있습니다.

   master와 iss53의 공통 조상은 C2 커밋입니다.

   ![image-20220225172602328](3일차강의자료.assets/image-20220225172602328-16457775633052.png)

2. 이 상황에서 master에 iss53을 병합하면 어떻게 될까요?

```bash
$ git switch master
Switched to branch 'master'
$ git merge iss53
**Merge made by the 'ort' strategy.**
index.html |    1 +
1 file changed, 1 insertion(+)
```

3. master와 iss53은 갈래가 나누어져 있기 때문에 Fast-Forward로 합쳐질 수 없습니다.

따라서 공통 조상인 C2와 각자가 가리키는 커밋인 C4, C5를 비교하여 3-way merge를 진행합니다.

![image-20220225172640769](3일차강의자료.assets/image-20220225172640769-16457776015483.png)

4. 이때 생긴 C6는 master와 iss53이 병합되면서 발생한 Merge Commit입니다.

5. 병합이 완료된 iss53은 더 이상 필요 없으므로 삭제합니다.

```bash
$ git branch -d iss53
Deleted branch iss53 (58sdf23).
```

---

3.Merge Conflict

- 병합하는 두 브랜치에서 `같은 파일의 같은 부분`을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못해서 발생하는 충돌(Conflict) 현상
- 결국은 사용자가 직접 내용을 선택해서 Conflict를 해결해야 합니다.

1. 현재 master는 C4 커밋을, iss53은 C5 커밋을 가리키고 있습니다.

   master와 iss53의 공통 조상은 C2 커밋입니다. `(3-way merge에서 상황과 같습니다)`

   ![image-20220225172835711](3일차강의자료.assets/image-20220225172835711-16457777165024.png)

2. 3-way merge와는 달리, 만약 master와 iss53이 `같은 파일의 같은 부분`을 수정하고 병합한다면 어떤 일이 발생할까요?

   ```bash
   $ git merge iss53
   Auto-merging index.html
   CONFLICT (content): Merge conflict in index.html
   Automatic merge failed; fix conflicts and then commit the result.
   ```

3. 충돌이 일어난 파일을 확인하기 위해 `git status`를 입력합니다.

   ```bash
   $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
   
       both modified:      index.html
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

4. `index.html`을 열어보면 아래와 같이 충돌 내역이 나옵니다.

   ```html
   <<<<<<< HEAD:index.html
   <div id="footer">contact : email.support@github.com</div>
   =======
   <div id="footer">
    please contact us at support@github.com
   </div>
   >>>>>>> iss53:index.html
   ```

5. `=======` 를 기준으로 위는 master의 내용, 아래는 iss53의 내용입니다.

   이 중 하나를 선택할 수도 있고, 둘 다 선택할 수도 있고, 아예 새롭게 작성할 수도 있습니다.

   ```html
   <div id="footer">
   please contact us at email.support@github.com
   </div>
   ```

6. 이후 git add와 git commit을 통해 병합한 내용을 커밋할 수 있습니다.

   ```bash
   $ git add .
   $ git commit
   ```

7. Vim 편집기를 이용해서 커밋 내역을 수정할 수 있습니다.

   ```bash
   Merge branch 'iss53'
   
   Conflicts:
       index.html
   #
   # It looks like you may be committing a merge.
   # If this is not correct, please remove the file
   #	.git/MERGE_HEAD
   # and try again.
   
   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   # On branch master
   # All conflicts fixed but you are still merging.
   #
   # Changes to be committed:
   #	modified:   index.html
   #
   ```

8. Vim 편집기를 통해 작성한 커밋이 이제 C6 커밋이 됩니다.

   ![image-20220225172848369](3일차강의자료.assets/image-20220225172848369-16457777293335.png)

9. 병합이 완료된 iss53은 더 이상 필요 없으므로 삭제합니다.

   ```bash
   $ git branch -d iss53
   Deleted branch iss53 (58sdf23).
   ```

## [2] Branch-merge Scenario

> 지금까지 학습했던 git merge와 세 가지 상황에 대해 다시 한 번 살펴봅니다.

### (1) 사전 세팅

```bash
$ mkdir git_merge
$ cd git_merge

$ git init
$ touch test.txt

# test.txt 에 master test 1 을 입력 후 저장

$ git add .
$ git commit -m "master test 1"
```

### (2) Fast-Forward

![image-20220225172921107](3일차강의자료.assets/image-20220225172921107-16457777617596.png)

<aside> 💡 **login 브랜치가 생성된 이후 master 브랜치에 변경 사항이 없는 상황**

즉, master 브랜치에서 login 브랜치를 merge 할 때 login 브랜치가 master 브랜치 이후의 커밋을 가리키고 있으면 그저 master 브랜치가 login 브랜치와 동일한 커밋을 가리키도록 이동 시킬 뿐입니다.

</aside>

1. `login` 브랜치 생성 및 이동합니다.

   ```bash
   $ git switch -c login
   ```

2. `login.txt`를 만들고 커밋합니다.

   ```bash
   $ touch login.txt
   $ git add .
   $ git commit -m "login test 1"
   ```

3. `master` 브랜치로 이동합니다.

   ```bash
   $ git switch master
   
   $ git log --oneline --all --graph
   * df231d0 (login) login test 1
   * 1e62b4c (HEAD -> master) master test 1
   ```

4. `master`에 `login`을 병합합니다.

   ```bash
   $ git merge login
   Updating 1e62b4c..df231d0
   **Fast-forward**
    login.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 login.txt
   ```

5. 결과를 확인합니다. (**Fast-forward**, 단순히 HEAD를 앞으로 빨리감기)

   ```bash
   $ git log --oneline --all --graph
   * df231d0 (HEAD -> master, login) login test 1
   * 1e62b4c master test 1
   ```

6. `login` 브랜치를 삭제합니다.

   ```bash
   $ git branch -d login
   Deleted branch login (was df231d0).
   
   $ git log --oneline --all --graph
   * df231d0 (HEAD -> master) login test 1
   * 1e62b4c master test 1
   ```

### (3) 3-way Merge (Merge commit)

![image-20220225172943489](3일차강의자료.assets/image-20220225172943489-16457777842057.png)

<aside> 💡 현재 브랜치(master)가 가리키는 커밋이 Merge 할 브랜치의 조상이 아니면, git은 각 브랜치가 가리키는 커밋 2개와 공통 조상 하나를 사용하며 `3-way Merge` 합니다.

단순히 브랜치 포인터를 최신 커밋으로 옮기는 게 아니라 3-way Merge 의 결과를 별도의 커밋으로 만들고 나서 해당 브랜치가 그 커밋을 가리키도록 이동 시킵니다. 그래서 이런 커밋은 부모가 여러 개고 `Merge commit` 이라고 합니다.

</aside>

1. `signout` 브랜치를 생성 및 이동합니다.

   ```bash
   $ git switch -c signout
   ```

2. 특정 작업 완료 후 커밋합니다.

   ```bash
   $ touch signout.txt
   
   $ git add .
   $ git commit -m "signout test 1"
   
   $ git log --oneline
   bcade83 (HEAD -> signout) signout test 1
   df231d0 (master) login test 1
   1e62b4c master test 1
   ```

3. `master` 브랜치로 이동합니다.

   ```bash
   $ git switch master
   ```

4. `master`에 추가 작업 후 커밋합니다. (단 **`signout` 브랜치와 다른 파일**을 생성 혹은 수정합니다.)

   ```bash
   $ touch master.txt
   
   $ git add .
   $ git commit -m "master test 2"
   
   $ git log --all --oneline
   48bd5a6 (HEAD -> master) master test 2
   bcade83 (signout) signout test 1
   df231d0 login test 1
   1e62b4c master test 1
   ```

5. `master`에 `signout`을 병합합니다. (자동 merge commit 발생)

   ```bash
   $ git merge signout
   Merge made by the 'ort' strategy.
    signout.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 signout.txt
   ```

6. log 확인

   ```bash
   $ git log --oneline --all --graph
   *   ac0e971 (HEAD -> master) Merge branch 'signout'
   |\\
   | * bcade83 (signout) signout test 1
   * | 48bd5a6 master test 2
   |/
   * df231d0 login test 1
   * 1e62b4c master test 1
   ```

7. `signout` 브랜치 삭제

   ```bash
   $ git branch -d signout
   Deleted branch signout (was bcade83).
   ```

### (4) Merge Conflict

![image-20220225173020122](3일차강의자료.assets/image-20220225173020122.png)

<aside> 💡 Merge 하는 두 브랜치에서 **같은 파일의 한 부분을 동시에 수정**하고 Merge 하면 Git은 해당 부분을 자동으로 Merge 하지 못하고 충돌이 일어납니다. **(반면 동일 파일이더라도 서로 다른 부분을 수정했다면, Conflict 없이 자동으로 Merge Commit 됩니다!)**

</aside>

1. `hotfix` 브랜치를 생성 및 이동합니다.

   ```bash
   $ git switch -c hotfix
   ```

2. 특정 작업 완료 후 커밋합니다.

   ```bash
   # test.txt 수정
   
   master test 1
   **이건 hotfix에서 작성한 문장입니다.**
   ```

   ```bash
   $ git add .
   $ git commit -m "hotfix test 1"
   
   $ git log --oneline --graph --all
   * ad045fa (HEAD -> hotfix) hotfix test 1
   *   ac0e971 (master) Merge branch 'signout'
   |\\
   | * bcade83 signout test 1
   * | 48bd5a6 master test 2
   |/
   * df231d0 login test 1
   * 1e62b4c master test 1
   ```

3. `master` 브랜치로 이동합니다.

   ```bash
   $ git switch master
   ```

4. 특정 작업(`hotfix` 와 동일 파일의 동일 부분 수정) 완료 후 커밋합니다.

   ```bash
   # text.txt 수정
   
   master test 1
   **이건 master에서 작성한 문장입니다.**
   ```

   ```bash
   $ git add .
   $ git commit -m "master test 3"
   
   $ git log --oneline --all --graph
   * 3170247 (HEAD -> master) master test 3
   | * ad045fa (hotfix) hotfix test 1
   |/
   *   ac0e971 Merge branch 'signout'
   |\\
   | * bcade83 signout test 1
   * | 48bd5a6 master test 2
   |/
   * df231d0 login test 1
   * 1e62b4c master test 1
   ```

5. `master`에 `hotfix`를 병합합니다.

   ```bash
   $ git merge hotfix
   ```

6. 결과 → merge conflict 발생 (**같은 파일의 같은 문장을 수정했기 때문입니다!**)

   ![image-20220225173033106](3일차강의자료.assets/image-20220225173033106.png)

7. 충돌 확인 및 해결

   - Merge Conflict가 일어났을 때 Git이 어떤 파일을 Merge 할 수 없었는지 살펴보려면 `git status` 명령을 이용합니다.

   ```bash
   $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

   ```
   master test 1
   <<<<<<< HEAD
   이건 master에서 작성한 문장입니다.
   =======
   이건 hotfix에서 작성한 문장입니다.
   >>>>>>> hotfix
   ```

   - `=======` 위쪽의 내용은 HEAD 버전(merge 명령을 실행할 때 작업하던 `master` 브랜치)의 내용이고 아래쪽은 `hotfix` 브랜치의 내용입니다. 충돌을 해결하려면 위쪽이나 아래쪽 내용 중에서 고르거나 새로 작성하여 Merge 해야 합니다. (`<<<<<<<, =======, >>>>>>>` 가 포함된 행은 삭제)

   ```bash
   # test.txt 최종본
   
   master test 1
   이건 충돌을 해결한 후의 문장입니다.
   ```

8. merge commit 진행합니다.

   ```bash
   $ git add .
   $ git commit
   ```

   - vim 편집기 등장

     ```bash
     Merge branch 'hotfix'
     
     # Conflicts:
     #       test.txt
     #
     # It looks like you may be committing a merge.
     # If this is not correct, please run
     #       git update-ref -d MERGE_HEAD
     # and try again.
     
     # Please enter the commit message for your changes. Lines starting
     # with '#' will be ignored, and an empty message aborts the commit.
     #
     # On branch master
     # All conflicts fixed but you are still merging.
     #
     ```

   - 작성된 커밋 메세지를 확인하고 `esc` 를 누른후 `:wq` 를 입력하여 저장 & 종료합니다.

     ```bash
     $ git commit
     [master 8ef1443] Merge branch 'hotfix'
     ```

9. log 확인

   ```bash
   $ git log --oneline --all --graph
   *   8ef1443 (HEAD -> master) Merge branch 'hotfix'
   |\\
   | * ad045fa (hotfix) hotfix test 1
   * | 3170247 master test 3
   |/
   *   ac0e971 Merge branch 'signout'
   |\\
   | * bcade83 signout test 1
   * | 48bd5a6 master test 2
   |/
   * df231d0 login test 1
   * 1e62b4c master test 1
   ```

10. `hotfix` 브랜치를 삭제합니다.

---

## [1] 원격 저장소 소유권이 있는 경우 (Shared repository model)

### (1) 개념

- 원격 저장소가 자신의 소유이거나 collaborator로 등록되어 있는 경우에 가능합니다.
- master에 직접 개발하는 것이 아니라, `기능별로 브랜치`를 따로 만들어서 개발합니다.
- `Pull Request`를 같이 사용하여 팀원 간 변경 내용에 대한 소통을 진행합니다.

### (2) 작업 흐름

1. 소유권이 있는 원격 저장소를 로컬 저장소로 `clone` 받습니다.

   ```bash
   $ git clone <https://github.com/edukyle/django-project.git>
   ```

2. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`합니다.

   ```bash
   $ git switch -c feature/login
   ```

3. 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 `push` 합니다.

   ```bash
   $ git push origin feature/login
   ```

4. 원격 저장소에는 master와 각 기능의 브랜치가 반영되었습니다.

5. Pull Request를 통해 브랜치를 master에 반영해달라는 요청을 보냅니다. (팀원들과 코드 리뷰를 통해 소통할 수 있습니다.)

6. 병합이 완료되면 원격 저장소에서 병합이 완료된 브랜치는 불필요하므로 삭제합니다.

7. master에 브랜치가 병합되면, 각 사용자는 로컬의 master 브랜치로 이동합니다.

   ```bash
   $ git switch master
   ```

8. 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 받아옵니다.

   ```bash
   $ git pull origin master
   ```

9. 병합이 완료된 master의 내용을 받았으므로, 기존 로컬 브랜치는 삭제합니다. (한 사이클 종료)

   ```bash
   $ git branch -d feature/login
   ```

10. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복합니다.

    ```bash
    $ git switch -c feature/pay
    ```

## [2] 원격 저장소 소유권이 없는 경우 (Fork & Pull model)

### (1) 개념

- 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우 사용합니다.
- 원본 원격 저장소를 그대로 내 원격 저장소에 `복제`합니다. (이 행위를 `fork`라고 합니다.)
- 기능 완성 후 `Push는 복제한 내 원격 저장소에 진행`합니다.
- 이후 `Pull Request`를 통해 원본 원격 저장소에 반영될 수 있도록 요청합니다.

### (2) 작업 흐름

1. 소유권이 없는 원격 저장소를 `fork`를 통해 내 원격 저장소로 `복제`합니다.

   아래와 같이 `Fork` 버튼을 누르면 자동으로 내 원격 저장소에 복제됩니다.

2. `fork` 후, 복제된 내 원격 저장소를 로컬 저장소에 `clone` 받습니다.

   ```bash
   $ git clone <https://github.com/edukyle/kakao_clone.git>
   ```

3. 이후에 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해서 연결합니다.

   ```bash
   # 원본 원격 저장소에 대한 이름은 upstream으로 붙이는 것이 일종의 관례
   
   $ git remote add upstream <https://github.com/AlexKwonPro/kakao_clone.git>
   ```

4. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`합니다.

   ```bash
   $ git switch -c feature/login
   ```

5. 기능 구현이 완료되면, `복제 원격 저장소(origin)`에 해당 브랜치를 `push` 합니다.

   ```bash
   $ git push origin feature/login
   ```

6. `복제 원격 저장소(origin)`에는 master와 브랜치가 반영되었습니다.

7. `Pull Request`를 통해 `복제 원격 저장소(origin)의 브랜치`를 `원본 원격 저장소(upstream)의 master`에 반영해달라는 요청을 보냅니다. (원본 원격 저장소의 관리자가 코드 리뷰를 진행하여 반영 여부를 결정합니다.)

8. `원본 원격 저장소(upstream)`의 master에 브랜치가 병합되면 `복제 원격 저장소(origin)`의 브랜치는 삭제합니다. 그리고 사용자는 로컬에서 master 브랜치로 이동합니다.

   ```bash
   $ git switch master
   ```

9. 병합으로 인해 변경된 `원본 원격 저장소(upstream)의 master` 내용을 로컬에 받아옵니다. 그리고 기존 로컬 브랜치는 삭제합니다. (한 사이클 종료)

   ```bash
   $ git pull upstream master
   $ git branch -d feature/login
   ```

10. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복합니다.

    ```bash
    $ git switch -c feature/pay
    ```

## [3] Pull Request (PR) 자세히 알아보기

> Github 화면을 통해 Pull Request 과정을 자세히 알아봅니다.

1. 브랜치를 Push 하면 `Compare & pull request` 라는 알림 버튼이 나타나는데, 이를 누르면 됩니다.

2. 혹은 원격 저장소 상단 바에서 `Pull requests → New pull request`을 통해서도 가능합니다.

3. `base`는 병합될 대상입니다. `master`를 `base`로 두면 됩니다. `compare`는 병합할 대상입니다. 우리가 만든 `feature/login` 브랜치를 `compare`로 두면 됩니다. 그리고 아래쪽에서 비교 내용을 확인하고 `Create pull request`를 클릭합니다.

4. Pull Request에 대한 제목과 내용, 각종 담당자를 지정하는 페이지가 나옵니다. 모두 작성했다면 `Create pull request`를 눌러서 PR을 생성합니다.

   `Reviewers` : 현재 PR에 대해 코드 리뷰를 진행해 줄 담당자

   `Assignees` : 현재 PR에 대한 작업을 맡고 있는 담당자

5. PR이 생성되면 다음과 같은 화면이 나타납니다. 빨간 표시가 된 세 부분을 살펴보겠습니다.

6. `Conversation` : 아래 Write 부분에서 comment를 별도로 작성할 수도 있습니다. 그리고 `Merge pull request` 버튼을 누르면 병합이 시작됩니다. (충돌(conflict) 상황에서는 충돌을 해결하라고 나옵니다.)

7. `Commits` : PR을 통해 반영될 커밋들을 볼 수 있습니다.

8. `Files changed` : 파일의 변화 내역들을 볼 수 있습니다.

9. 코드리뷰를 원하는 라인에서 `+` 를 눌러서 해당 라인에 리뷰를 남길 수 있습니다.

   빨간 사각형으로 표시된 작은 아이콘을 클릭하면, **`suggestion 기능`(코드를 이렇게 바꾸라고 추천하는 기능)**을 넣을 수도 있습니다.

10. 코드 리뷰를 끝내려면 `Finish your review` 버튼을 누르면 됩니다. 그리고 옵션을 선택하고 `Submit review`를 클릭합니다.

    - `Comment`: 추가적인 comment를 작성할 경우 선택
    - `Approve`: merge를 승인하는 경우 선택
    - `Request change` : 수정해야 하는 사항이 있을 경우 선택

11. 다시 conversation으로 가보면 진행했던 리뷰가 이렇게 나타난 것을 확인할 수 있습니다.

12. 병합을 하게 되면 아래와 같이 보라색으로 병합이 완료되었다고 나오면 성공입니다.

    `Delete branch` 버튼을 통해 병합된 `feature/login` 브랜치를 지울 수 있습니다. (원격 저장소에서만 지워집니다.)

13. `master`를 확인해보면 `feature/login`의 내용이 master에 병합된 것을 확인할 수 있습니다.

14. 이후 로컬 저장소의 master 브랜치에서 `git pull`을 이용해 로컬과 원격을 동기화 합니다.

## [4] 실습

> 백일장 실습을 통해 소유권이 없는 상태에서의 협업하는 방법(fork 와 pull request)에 대해 익혀 봅시다.

1. 특강 페이지에 공유된 `acrostic-poem` repository를 fork합니다.
2. 참가자는 forked repository를 `clone`하여 본인 local에 복제합니다.
3. `학생 이름`으로 된 브랜치를 생성하고, 주어진 명제에 따라 N행시를 작성해 봅시다.
4. 작성을 완료한 결과물에 대해 브랜치를 `push` 합니다. 이 때, 본인의 repository로 보내야 합니다.
5. github에서 강사님의 repository에 Pull & request 를 보내 봅시다.

<aside> 📌 **순서**

`fork`→`clone`→브랜치 생성→ `add` → `commit` → 브랜치 `push` → `pull&request` 보내기

</aside>