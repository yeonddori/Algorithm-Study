import sys
input = sys.stdin.readline

original = list(input().rstrip())
M = int(input())
right = []

for _ in range(M):
    command = list(input().split())
    if command[0] == 'P':
        char = command[1]
        original.append(char)

    elif command[0] == 'L' and original:
        right.append(original.pop())

    elif command[0] == 'D' and right:
        original.append(right.pop())

    elif command[0] == 'B' and original:
        original.pop()

result = original + right[::-1]
result = ''.join(result)
print(result)

# 하 이렇게 푸는거 생각을 어떻게 하지???
# 너무 답답하다.