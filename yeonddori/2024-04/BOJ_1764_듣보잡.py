N, M = map(int, input().split())
not_hear = {input() for _ in range(N)}
not_see = {input() for _ in range(M)}

not_hear_see = (not_hear & not_see)

print(len(not_hear_see))
for name in sorted(not_hear_see):
    print(name)
