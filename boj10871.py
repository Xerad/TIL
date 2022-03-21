N, X = list(map(int, input().split()))  # 첫 번째 줄 정수 N, X 입력
A = list(map(int, input().split())) # 두 번째 줄 정수 A 입력

for i in range(N):
    if A[i] < X: # A에서 X보다 작은 수
        print(A[i], end = ' ') 