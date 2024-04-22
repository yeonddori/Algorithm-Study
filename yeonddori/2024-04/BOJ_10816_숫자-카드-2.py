def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return right


def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return right


N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(upper_bound(cards, num) - lower_bound(cards, num), end=' ')
