color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
value = [x for x in range(10)]
mul = [pow(10,x) for x in range(0,10)]

result = 1

a = input()
for i in range(len(color)):
    if color[i] == a:
        result *= value[i]*10
b = input()
for i in range(len(color)):
    if color[i] == b:
        result += value[i]
c= input()
for i in range(len(color)):
    if color[i] == c:
        result *= mul[i]
print(result)
