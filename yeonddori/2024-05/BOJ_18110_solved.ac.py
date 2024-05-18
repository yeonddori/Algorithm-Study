import sys


def round_num(num):
    if num - int(num) >= 0.5:
        num = int(num) + 1
    else:
        num = int(num)
    return num


n = int(sys.stdin.readline())
if n == 0:
    print(0)
    exit()

nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

remove = round_num(n * 0.15)
print(round_num(sum(nums[remove:n - remove]) / (n - 2 * remove)))
