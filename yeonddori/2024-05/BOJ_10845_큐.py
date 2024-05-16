import sys
N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        print(queue.pop(0) if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)
