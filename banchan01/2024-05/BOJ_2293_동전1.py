n, k = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

# dp[i] 정의 -> 숫자 i를 나타낼 수 있는 경우의 수
dp = [0] *(k+1)
dp[0] = 1

# 4를 만들때, 112, 121, 211 같이 구성이 같은 것들은 다 똑같다고 취급 해야함.
# x + lst요소 << 로 처리하면 해결됨.
# ex) 문제 예제에서, lst = [1,2,5]
# dp[6]을 구하고 싶다!!! 하면
# 6 = 5 + '1', 4 + '2' , 6 = 1 + '5' 임.
# 따옴표 한 숫자들은 그냥 ㄹㅇ 그 숫자 자체만 젤 뒤에 더해주는 거임.
# ex) 4 + '2'
# 4를 만들어주는 경우의 수 + 2

for j in lst:
    for i in range(1,k+1):
        if i-j>=0:
            dp[i] += dp[i-j]
print(dp[k])