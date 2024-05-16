n = int(input())

lst = [0] * (n+1)
for i in range(1,n+1):
    lst[i] = int(input())
# dp[i] 정의 -> i번째 인덱스까지 판단했을때, 최대 포도주 양
dp = [0]*(n+1)
dp[1] = lst[1]

if n > 1:
    dp[2] = lst[1] + lst[2]

for i in range(3, n + 1):
    # 전 포도주 먹는경우 vs 안먹는 경우
    dp[i] = max(dp[i - 2], dp[i - 3] + lst[i - 1]) + lst[i]
    # ex) 순서대로 2억 , 1억, 1, 5 이 순서로 포도주가 있다 하자,
    # 위의 코드는 2억 or 1억을 포기하고 1을 무조건 먹게되는 구조..
    # 나는 2억 & 1억 먹고, 1 버리고, 5먹고 싶은데??
    # 현재 고려대상인 인덱스를 안먹는 경우... 추가 해주기
    # 어려움....
    dp[i] = max(dp[i-1], dp[i])

print(dp[n])