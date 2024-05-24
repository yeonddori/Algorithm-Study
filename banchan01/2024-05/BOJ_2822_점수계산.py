score = []
for _ in range(8):
    score.append(int(input()))

s_score = sorted(score,reverse = True)
total_score = sum(s_score[:5])

result = []

for i in range(8):
    if score[i] in s_score[:5]:
        result.append(i+1)
print(total_score)
for number in result:
    print(number, end = ' ')