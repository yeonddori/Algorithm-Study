# 50점코드
n = int(input())
m = int(input())
s = input()

standard = ['I']
o_cnt = 0
while o_cnt != n:
    if standard[-1] == 'I':
        standard.append('O')
    else:
        standard.append('I')
        o_cnt += 1
standard = ''.join(standard)

result = 0
for i in range(m):
    if s[i] == 'I':
        if s[i:i+(2*n+1)] == standard:
            result += 1
print(result)

# 100점 코드
n = int(input())
m = int(input())
s = input()

i, cnt, result = 0, 0, 0
while i < m-2:
    if s[i:i+3] == 'IOI':
       cnt += 1
       i += 2
       if cnt == n:
           result += 1
           cnt -= 1
    else:
        cnt = 0
        i += 1

print(result)
