S = int(input())

hap = 0
big = 0
while( hap<=S ):
    big += 1
    hap = big * (big+1) / 2

print(big-1)