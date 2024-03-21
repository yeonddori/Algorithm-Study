n  = int(input())

# 오름차순으로 숫자넣는 리스트
stack = []

# 결과 담는 리스트
result = []

first = 1

# 문제에서 주어진 수열 리스트 생성
sequence = []
for _ in range(n):
    sequence.append(int(input()))


for i in sequence:

    if(first <= i):
        while(first <= i):
            stack.append(first)
            result.append('+')
            first += 1

    if (stack[-1] == i):
        stack.pop(-1)
        result.append('-')
    else:
        result = ['NO']
        break

for i in result:
    print(i)