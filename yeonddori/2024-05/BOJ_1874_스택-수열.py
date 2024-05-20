import sys

n = int(sys.stdin.readline())
stack = []
result = []
count = 1
flag = True

for _ in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if flag:
    for i in result:
        print(i)
else:
    print('NO')
