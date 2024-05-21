import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == 'all':
            S = set(range(1, 21))
        else:
            S = set()
    else:
        command, x = command[0], int(command[1])
        if command == 'add':
            S.add(x)
        elif command == 'remove':
            S.discard(x)
        elif command == 'check':
            print(1 if x in S else 0)
        elif command == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
