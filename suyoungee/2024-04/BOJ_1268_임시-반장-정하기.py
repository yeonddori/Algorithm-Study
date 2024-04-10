N = int(input())
students = []
for i in range(N):
    students.append([int(j) for j in input().split()])

max_friend = -1
leader = -1
for student_id in range(N):
    result =set()
    for grade in range(5):
        for friend in range(N):
            if students[student_id][grade] == students[friend][grade]:
                result.add(friend)               
    
    if len(result) > max_friend:
        leader = student_id +1
        max_friend = len(result)
        

print(leader)