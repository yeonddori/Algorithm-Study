def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
cards.sort()

for target in targets:
    print(binary_search(cards, target), end=' ')
