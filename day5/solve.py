import re

f1 = open("crates.txt", "r")
map = {i + 1: [] for i in range(9)}
pos = []
x_locations = {}
row = 0
for line in f1.readlines():
    dist = 0
    for char in line:
        if char in "123456789":
            x_locations[dist] = int(char)
        elif char not in "[ ]\n":
            pos.append([char, dist])

        dist += 1


for entry in pos:
    x_i = x_locations[entry[1]]
    map[x_i] = [entry[0]] + map[x_i]


def move_crate(num, l1, l2):
    items = map[l1][-num:]
    map[l1] = map[l1][:-num]
    map[l2] = map[l2] + items


f2 = open("moves.txt")

for line in f2.readlines():
    num_match = re.search("move \d+ ", line)[0]
    num = int(re.search("\d+", num_match)[0])
    l1_match = re.search("from \d ", line)[0]
    l1 = int(re.search("\d", l1_match)[0])
    l2_match = re.search("to \d", line)[0]
    l2 = int(re.search("\d", l2_match)[0])
    move_crate(num, l1, l2)
ans = ""
for loc, crates in map.items():
    print(loc, crates[-1])
    ans = ans + crates[-1]

print(ans)
