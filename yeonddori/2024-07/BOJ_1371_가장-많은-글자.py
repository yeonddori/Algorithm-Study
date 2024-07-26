import sys

words = sys.stdin.read().split()
words = ''.join(words)
alphabet = [0] * 26

for word in words:
    alphabet[ord(word) - ord('a')] += 1

max_alphabet = max(alphabet)
for i in range(26):
    if alphabet[i] == max_alphabet:
        print(chr(i + ord('a')), end='')
