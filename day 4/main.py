from collections import defaultdict
from functools import reduce
# # Part 1
with open('day 4\input.txt') as f:
    s = f.read().splitlines()

r= 0
# s = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """
# s = s.strip().split('\n')
##################### Part 1
for i, line in enumerate(s):
    winners, game = line.split('|')
    winners = winners.split(':')[1].strip()
    game.strip()
    game = [int(num) for num in  game.split()]
    winners = [int(num) for num in  winners.split()]
    win_numbers = list(set(game).intersection(winners))
    card = 0
    for i in range(len(win_numbers)):
        card = 2 ** i
    r += card
print(r)
r2 = 0
card_ids, card_list= [], []
################## Part 2
for line in s:
    card_id, winners = line.split(':')
    card_ids.append(card_id)
    card_list.append(1)
for i, line in enumerate(s):
    card_id, winners = line.split(':')
    winners, game = winners.split('|')
    game.strip()
    game = [int(num) for num in  game.split()]
    winners = [int(num) for num in  winners.split()]
    win_numbers = list(set(game).intersection(winners))
    index, old_index = card_ids.index(card_id), card_ids.index(card_id)
    for _add in range(len(win_numbers)):
        index += 1 
        card_list[index] += 1 * card_list[old_index]
        r += 1
print(sum(card_list))