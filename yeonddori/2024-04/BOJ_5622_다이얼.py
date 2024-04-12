dial = input()
dial_time = 0

for i in dial:
    if i in ['A', 'B', 'C']:
        dial_time += 3
    elif i in ['D', 'E', 'F']:
        dial_time += 4
    elif i in ['G', 'H', 'I']:
        dial_time += 5
    elif i in ['J', 'K', 'L']:
        dial_time += 6
    elif i in ['M', 'N', 'O']:
        dial_time += 7
    elif i in ['P', 'Q', 'R', 'S']:
        dial_time += 8
    elif i in ['T', 'U', 'V']:
        dial_time += 9
    elif i in ['W', 'X', 'Y', 'Z']:
        dial_time += 10

print(dial_time)
