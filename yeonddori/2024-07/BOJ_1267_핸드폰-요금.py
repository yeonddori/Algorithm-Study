N = int(input())
calls = list(map(int, input().split()))

Y = 0
M = 0

for call in calls:
    Y += (call // 30 + 1) * 10
    M += (call // 60 + 1) * 15

if Y < M:
    print("Y", Y)
elif Y > M:
    print("M", M)
else:
    print("Y M", Y)
