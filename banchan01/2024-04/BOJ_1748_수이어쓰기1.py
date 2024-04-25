n = input()
# 자릿수
length = len(n)
# 결과 정의
result = 0
# 주어진 숫자 자릿수-1 의 자릿수 모두 더하기
for i in range(1,length):
    mini_len = pow(10,i) - pow(10,i-1)
    result += mini_len * i

result += (int(n) - pow(10,length-1) + 1) * length

print(result)