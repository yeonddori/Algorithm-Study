def solution(cards1, cards2, goal):
    for i in range(0,len(cards1), 1):
        a = cards1[i]
        for j in range(0, len(goal), 1):
            if cards1[i] == goal[j]:
                cards1[i] = int(j)
        if cards1[i] == a:
            cards1[i] = 100
            
    for i in range(0,len(cards2), 1):
        b = cards2[i]
        for j in range(0, len(goal), 1):
            if cards2[i] == goal[j]:
                cards2[i] = int(j) 
        if cards2[i] == b:
            cards2[i] = 100
    sort_cards1 = sorted(cards1)
    print(cards1)
    print(sort_cards1)
    sort_cards2 = sorted(cards2)
    print(cards2)
    print(sort_cards2)
    if (sort_cards1 == cards1) and (sort_cards2 == cards2): 
        answer = 'Yes'
    else:
        answer = "No"
    return answer