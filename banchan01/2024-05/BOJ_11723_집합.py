import sys
input = sys.stdin.readline

def add(S,n):
    if n in S:
        pass
    else:
        S.append(n)

def remove(S,n):
    if n in S:
        S.remove(n)
    else:
        pass

def check(S,n):
    if n in S:
        print(1)
    else:
        print(0)

def toggle(S,n):
    if n in S:
        S.remove(n)
    else:
        S.append(n)

def all(S):
    S.clear()
    S.extend(range(1, 21))

def empty(S):
    S.clear()

def main():
    S = []
    m = int(input())

    for _ in range(m):
        command = input().strip().split()
        char = command[0]

        if char in ['add','remove','check','toggle']:
            n = int(command[1])

            if char == 'add':
                add(S, int(n))

            elif char == 'remove':
                remove(S, int(n))

            elif char == 'check':
                check(S, int(n))

            elif char == 'toggle':
                toggle(S, int(n))

        elif char == 'all':
            all(S)

        elif char == 'empty':
            empty(S)

main()