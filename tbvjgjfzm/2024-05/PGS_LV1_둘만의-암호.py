import string
def solution(s, skip, index):
    answer = ''
    alphabet_lower = string.ascii_lowercase
    l_alphabet = list(alphabet_lower)
    n_skip = list(skip)
    print(l_alphabet)
    print(n_skip)
    for i in range(0, len(skip)):
        l_alphabet.remove(n_skip[i])
    for j in range(0, len(s)):
        k = l_alphabet.index(s[j])
        if k + index + 1 < len(l_alphabet):
            answer += l_alphabet[k+index]
        elif k + index + 1 == len(l_alphabet):
            answer += l_alphabet[k+index]
        else:
            answer += l_alphabet[(k+index)%len(l_alphabet)]
    return answer