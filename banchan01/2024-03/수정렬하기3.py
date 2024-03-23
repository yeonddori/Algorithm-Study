import sys
n = int(sys.stdin.readline())

dic = {}

# Initialize all dic's values to 0
for i in range(1,10001):
    dic[i] = 0

# Update dic's values
for _ in range(n):
    dic[int(sys.stdin.readline())] += 1

for i in dic:
    if (dic[i] != 0):
        for _ in range(dic[i]):
            print(i)
