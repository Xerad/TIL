# introspection

- ? : 객체 정보 출력
- ?? : 소스코드 까지 출력(가능하면)

``` python
a = [1,2,3,4]
a?

plt.ylim?

a(shift + tab)

print??

np.*load*?
```

# 매직 명령어

- 앞에 % 기호를 붙여서 사용한다.
- %magic : 모든 매직함수의 도움말
- %time <code> : 코드 단일 실행후 시간 출력
- %timeit <code> : 코드를 반복실행 후 평균 시간 출력
- %env <code> : 환경변수 출력
- %matplotlib : 그래프를 노트북에 띄울수 있도록 해준다(기본설정이라 따로 입력해줄 필요는 없음)

```python
%time [i for i in range(100000)]

%pwd

%env
```

# 운영체제 명령어

- ! : 시스템 명령어를 실행한다.

```python
!dir

!ipconfig

!pip install numpy
```

