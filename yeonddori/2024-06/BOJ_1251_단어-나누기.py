word = input()
answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        answer.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

answer.sort()
print(answer[0])
