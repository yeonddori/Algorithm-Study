import sys


def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in lan:
            cnt += i // mid
        if cnt >= N:
            left = mid + 1
        else:
            right = mid - 1
    return right


K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

print(binary_search(1, max(lan)))
