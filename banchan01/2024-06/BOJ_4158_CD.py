import sys
input=sys.stdin.readline

while 1:
    n,m=map(int,input().split())

    if n==0 and m==0:
        exit(0)

    n_lst=[]
    m_lst=[]

    for i in range(n):
        n_lst.append(int(input()))

    for i in range(m):
        m_lst.append(int(input()))

    n_idx=0
    m_idx=0
    result=0
    while n_idx<n and m_idx<m:

        if n_lst[n_idx]==m_lst[m_idx]:
            result+=1
            n_idx+=1
            m_idx+=1

        elif n_lst[n_idx]>m_lst[m_idx]:
            m_idx+=1
        else:
            n_idx+=1

    print(result)