A, B = map(int, input().split())

min_val = int(str(A).replace('6', '5')) + int(str(B).replace('6', '5'))
max_val = int(str(A).replace('5', '6')) + int(str(B).replace('5', '6'))

print(min_val, max_val)
