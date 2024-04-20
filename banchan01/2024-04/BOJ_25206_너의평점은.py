report =[]
grades = []
sisues = []

for i in range(20):
    report.append(input())

# �ü��� ���� list�� ���
for sentence in report:
    temp = sentence.split()
    sisues.append(temp[1])
    grades.append(temp[2])

# �ü� �� �� ���ϱ�
sisu_sum = 0
for i in range(len(sisues)):
    if grades[i] != 'P':
        sisu_sum += float(sisues[i])

# ������ ������ ��ȯ��Ű��
grades_mapping = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F' : 0.0,
    'P' : 0.0
}

for i in range(len(grades)):
    grades[i] = grades_mapping[grades[i]]


# ��� ���ϱ�
average_score = sum(float(x) * y for x,y in zip(sisues,grades)) / sisu_sum
r_average_score = "{:.6f}".format(average_score)
print(r_average_score)