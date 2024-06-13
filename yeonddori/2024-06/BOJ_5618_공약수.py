import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
g = gcd(nums[0], gcd(nums[1], nums[-1]))

for i in range(1, g//2 + 1):
    if g % i == 0:
        print(i)

print(g)
