text = input()

while text != '#':
    cnt = 0
    for i in text:
        if i.lower() in 'aeiou':
            cnt += 1
    print(cnt)
    text = input()
