# Brute Force String Match
word = 'ATENCAO ESSE E UM AVISO IMPORTANTE'
pattern = 'VISO'
n = len(word)
m = len(pattern)

for i in range(0, n-m+1):
    j = 0
    while (j<m and pattern[j] == word[i + j]):
        j = j + 1
    if (j == m):
        print(i)