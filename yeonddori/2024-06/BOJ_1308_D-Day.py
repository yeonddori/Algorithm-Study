from datetime import date

today = list(map(int, input().split()))
D_day = list(map(int, input().split()))

start = date(today[0], today[1], today[2])
end = date(D_day[0], D_day[1], D_day[2])

if end >= date(today[0] + 1000, today[1], today[2]):
    print("gg")
else:
    print(f"D-{(end - start).days}")
