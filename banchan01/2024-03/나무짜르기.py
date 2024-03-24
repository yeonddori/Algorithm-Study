import sys
n, m = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

left = 1
right = max(tree)

while(left<=right):
    got_tree = 0
    mid = (left+right)//2

    for i in tree:
        if (i - mid >= 0):
            got_tree += ( i-mid )

    if(got_tree>=m):
        left = mid + 1
    else:
        right = mid - 1

print(right)