def Rev(n):
    n = n[::-1]
    return int(n)

def main():
    a, b = input().split()
    tmp = Rev(a) + Rev(b)
    result = Rev(str(tmp))
    print(result)

main()