n = int(input())
original = list(map(int,input().split()))
compressed = sorted(set(original),reverse = True)

dic = {value: len(compressed)-1 - index for index, value in enumerate(compressed)}

result = [dic[num] for num in original]

for ans in result:
    print(ans, end = ' ')