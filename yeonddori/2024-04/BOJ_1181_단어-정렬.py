N = int(input())
words = [i for i in set(input() for _ in range(N))]
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
