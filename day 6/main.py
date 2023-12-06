from collections import defaultdict
from functools import reduce
from math import comb
# # Part 1
with open('day 6\input.txt') as f:
    s = f.read().splitlines()

##################### Part I
to_check = []
ans = 0
times = s[0].split(':')[1].strip().split()
dist = s[1].split(':')[1].strip().split()
for i, time in enumerate(times):
    dt, cnt, won = int(time), 0, 0
    while dt > 0:
        win = cnt * dt
        if win > int(dist[i]):
            won += 1
        dt -= 1
        cnt += 1
    to_check.append(won)
print(reduce(lambda x, y: x * y, to_check))
# PART II

to_check = []
time = s[0].split(':')[1].strip()
dist = s[1].split(':')[1].strip()
time = int("".join(time.split()))
dist = int("".join(dist.split()))
# ans2 = 1  # assuming there's atleast always 1 way
# for t, dist in zip([new_time], [new_dist]):
#     ans2 *= sum(
#         ((t - hold_down_time) * hold_down_time) > dist
#         for hold_down_time in range(1, t)
#     )
# print(ans2)
ans = 0
for x in range(time+1):
    dx = x*(time-x)
    if dx>=dist:
        ans += 1
print(ans)  

