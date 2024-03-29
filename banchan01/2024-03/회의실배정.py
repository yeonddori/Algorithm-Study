n = int(input())

reservation = []
for _ in range(n):
    reservation.append(list(map(int,input().split())))

# increase sort with end-time
S_reservation = sorted(reservation,key=lambda x:(x[1],x[0]))
result = 1

# delare 당첨time
successful_time = S_reservation[0]

# 당첨time's end-time 보다 같거나 큰 time을 당첨time 으로 update
for i in range(1,n):
    if (successful_time[1] <= S_reservation[i][0]):
        successful_time = S_reservation[i]
        result += 1

print(result)