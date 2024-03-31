expression = input().split('-')

result = 0

for i in expression[0].split('+'):
    result += int(i)

for i in expression[1:]:
    a = i.split('+')
    for j in a:
        result -= int(j)

print(result)