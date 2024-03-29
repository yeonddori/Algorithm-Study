n = int(input())

reservation = []
for _ in range(n):
    reservation.append(list(map(int,input().split())))

# increase sort with end-time
S_reservation = sorted(reservation,key=lambda x:(x[1],x[0]))
result = 1

# delare ��÷time
successful_time = S_reservation[0]

# ��÷time's end-time ���� ���ų� ū time�� ��÷time ���� update
for i in range(1,n):
    if (successful_time[1] <= S_reservation[i][0]):
        successful_time = S_reservation[i]
        result += 1

print(result)