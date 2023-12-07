from collections import defaultdict
from functools import reduce
from math import comb
# # Part 1
with open('day 7\input.txt') as f:
    s = f.read().splitlines()
mapper = {
    'A': '14',
    'K': '13',
    'Q': '12',
    'J': '11',
    'T': '10',
}
##################### Part I

matrix  = [[], [], [], [], []]
n = len(s)
for i in range(n):
    hand, values = s[i].split()
    char_count = {}
    for char in hand:
        char_count[char] = char_count.get(char, 0) + 1
    type = max(char_count.values())
    matrix[type - 1].append((hand, values))
    
cnt = 0
for i in range(len(matrix[cnt])):
    for j in range(n - i - 1):
        h1 = matrix[cnt][j][0]
        if j + 1 < n - i - 1:
            h2 = matrix[cnt][j + 1][0]
        for n in range(len(matrix[cnt][j][0])):
            l1 = matrix[cnt][j][0][n]
            l2 = matrix[cnt][j + 1][0][n]
            if l1 in mapper:
                l1 = mapper[matrix[cnt][j][0][n]]
            if l2 in mapper:
                l2 = mapper[matrix[cnt][j + 1][0][n]]
            if int(l1) > int(l2):
                 matrix[cnt][j], matrix[cnt][j + 1] = matrix[cnt][j + 1], matrix[cnt][j]
                 break
            elif l1 == l2:
                continue
            else:
                break
    print(1)