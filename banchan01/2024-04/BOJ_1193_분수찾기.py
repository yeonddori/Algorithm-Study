x = int(input())

category = 1
def hap(a):
    return a*(a+1)//2

while( hap(category) < x ):
    category += 1

# �� catgory ������ �ִ� ���ϱ�
pre_max = hap(category-1)

# ����
son = x - pre_max
# �и�
mother = category+1 - son

if(category%2==0):
    print(f'{son}/{mother}')
else:
    print(f'{mother}/{son}')