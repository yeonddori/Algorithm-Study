N = int(input())
# 2차원 리스트로 초기화
dp = [[0]*3 for _ in range(N+1)]

# 새로운 행 추가되는 경우의 수는 3가지가 있음.
# 1. 사자 추가 X,  2. 왼쪽에 추가,  3. 오른쪽에 추가
# 각각 순서대로 0,1,2 라는 idx 가지게 할거임
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2,N+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]

    # (A + B) mod C = (A mod C + B mod C) mod C
    # 숫자 너무 커져서 메모리초과 방지!
    dp[i][0] %= 9901
    dp[i][1] %= 9901
    dp[i][2] %= 9901

result = dp[N][0] + dp[N][1] + dp[N][2]

print(result % 9901)