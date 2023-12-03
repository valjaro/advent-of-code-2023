
from collections import defaultdict
from functools import reduce
# # Part 1
with open('day 3\input.txt') as f:
    s = f.read().splitlines()
    
def check_adjacents(i, jlist, m, n):
    posible = False
    adjacent_indices = []
    for j in jlist: 
        if i > 0: # down
            adjacent_indices.append((i-1,j))
        if i + 1 < m: # top
            adjacent_indices.append((i+1,j))
        if j > 0: # left
            adjacent_indices.append((i,j-1))
        if j + 1 < n: # right
            adjacent_indices.append((i,j+1))
        if i > 0 and j > 0: # top-left
            adjacent_indices.append((i-1,j-1))
        if i > 0 and j+1 < n: # top-right
            adjacent_indices.append((i-1,j+1))
        if i + 1 < m and j > 0: # down-left
            adjacent_indices.append((i+1,j-1))
        if i + 1 < m and j+1 < n: # down-right
            adjacent_indices.append((i+1,j+1))
    for k, l in adjacent_indices:
        if s[k][l] != '.' and s[k][l] not in '0123456789':
            posible = True
            break
    return posible

r = 0
numbers = []
for i in range(0, len(s)):
    for j in range(0, len(s[i])):
        posible = False
        jlist = []
        num = ''
        if s[i][j].isdigit():
            while j < len(s[i]) and s[i][j] in '0123456789':
                num += s[i][j]
                jlist.append(j)
                s[i] = list(s[i])
                s[i][j] = '.'
                s[i] = "".join(s[i])
                j += 1
            posible = check_adjacents(i, jlist, len(s) - 1, len(s[i]) - 1)
        if posible:
            # numbers.append(num)
            # print(num)
            r += int(num)
# print(numbers)
print(r)
######## PART 2
with open('day 3\input.txt') as f:
    s2 = f.read().splitlines()
def multiply(x, y):
    return x * y
def check_adjacents2(i, jlist, m, n, num):
    posible = False
    adjacent_indices = []
    for j in jlist: 
        if i > 0: # down
            adjacent_indices.append((i-1,j))
        if i + 1 < m: # top
            adjacent_indices.append((i+1,j))
        if j > 0: # left
            adjacent_indices.append((i,j-1))
        if j + 1 < n: # right
            adjacent_indices.append((i,j+1))
        if i > 0 and j > 0: # top-left
            adjacent_indices.append((i-1,j-1))
        if i > 0 and j+1 < n: # top-right
            adjacent_indices.append((i-1,j+1))
        if i + 1 < m and j > 0: # down-left
            adjacent_indices.append((i+1,j-1))
        if i + 1 < m and j+1 < n: # down-right
            adjacent_indices.append((i+1,j+1))
    for k, l in adjacent_indices:
        if s2[k][l] == '*':
            cnts[(k, l)].append(int(num))
            break
r = 0
numbers = []
cnts = defaultdict(list)
for i in range(0, len(s2)):
    for j in range(0, len(s2[i])):
        posible = False
        jlist = []
        num = ''
        if s2[i][j].isdigit():
            while j < len(s2[i]) and s2[i][j] in '0123456789':
                num += s2[i][j]
                jlist.append(j)
                s2[i] = list(s2[i])
                s2[i][j] = '.'
                s2[i] = "".join(s2[i])
                j += 1
            check_adjacents2(i, jlist, len(s) - 1, len(s[i]) - 1, num)
for values in cnts.values():
    if len(values) > 1:
        r += reduce(multiply, values)
print(r)

