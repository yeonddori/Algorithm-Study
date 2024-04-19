x = int(input())

category = 1
def hap(a):
    return a*(a+1)//2

while( hap(category) < x ):
    category += 1

# 전 catgory 에서의 최댓값 구하기
pre_max = hap(category-1)

# 분자
son = x - pre_max
# 분모
mother = category+1 - son

if(category%2==0):
    print(f'{son}/{mother}')
else:
    print(f'{mother}/{son}')