lst = []

def main():
    T = int(input())

    # Initialize a 2 dimension array with 0.
    for i in range(15):
        if(i==0):
            lst.append(list(x for x in range(1,15)))
        else:
            lst.append(list(0 for _ in range(14)))

    # fill out array   
    for i in range(1,15):
        for j in range(14):
            lst[i][j] = sum(lst[i-1][:j+1])

    # Execute Find function T times
    for _ in range(T):
        Find()

def Find():
    k = int(input())
    n = int(input())
    n -= 1

    print(lst[k][n])

main()