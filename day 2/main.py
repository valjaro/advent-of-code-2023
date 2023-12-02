# # Part 1
with open('day 2\input.txt') as f:
    s = f.read()
# s = """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """
ids = 0
######### PART 1
for i in s.strip().split("\n"):
    id, g = i.split(":")
    id = int(id.split(" ")[1])
    # print(id)
    big = False
    blue, red, green = 0, 0, 0
    for y,l in enumerate(g):
        # print(g[y::])
        if g[y::].startswith('blue'):
            blue = int(g[y-3] + g[y-2])
        elif g[y::].startswith('red'):
            red = int(g[y-3] + g[y-2])
        elif g[y::].startswith('green'):
                green = int(g[y-3] + g[y-2])
        if red > 12 or green > 13 or blue > 14:
            big = True
            break
    if not big:
        ids += id
print(ids)
# #### ###Part 2
ids_2 = 0
for i in s.strip().split("\n"):
    id, g = i.split(":")
    id = int(id.split(" ")[1])
    big = False
    blue, red, green = 0, 0, 0
    for y,l in enumerate(g):
        if g[y::].startswith('blue'):
            if int(g[y-3] + g[y-2]) > blue:
                blue = int(g[y-3] + g[y-2])
        elif g[y::].startswith('red'):
            if int(g[y-3] + g[y-2]) > red:
                red = int(g[y-3] + g[y-2])
        elif g[y::].startswith('green'):
            if int(g[y-3] + g[y-2]) > green:
                green = int(g[y-3] + g[y-2])
    # print((red * green * blue))
    ids_2 += (red * green * blue)
print(ids_2)