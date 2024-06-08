N, Jimin, Hansu = map(int, input().split())
round = 0

while Jimin != Hansu:
    Jimin = (Jimin + 1) // 2
    Hansu = (Hansu + 1) // 2
    round += 1

print(round)
