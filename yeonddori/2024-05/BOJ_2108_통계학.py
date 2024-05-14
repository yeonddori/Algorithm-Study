import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

numbers_count = {}
for number in numbers:
    numbers_count[number] = numbers_count.get(number, 0) + 1
max_count = max(numbers_count.values())
max_numbers = [number for number, count in numbers_count.items()
               if count == max_count]

print(round(sum(numbers) / N))
print(numbers[N // 2])
print(max_numbers[0] if len(max_numbers) == 1 else max_numbers[1])
print(numbers[-1] - numbers[0])
