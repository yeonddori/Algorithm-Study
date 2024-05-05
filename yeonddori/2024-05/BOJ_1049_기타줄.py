N, M = map(int, input().split())
package = []
single = []

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

package.sort()
single.sort()

if single[0] * 6 < package[0]:
    print(single[0] * N)
else:
    if (N % 6) * single[0] < package[0]:
        print((N // 6) * package[0] + (N % 6) * single[0])
    else:
        print((N // 6 + 1) * package[0])
