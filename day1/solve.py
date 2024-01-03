import re

input = open("input.txt")
Lines = input.readlines()
all_elves = [[]]
for line in Lines:
    if re.search("^\d", line) is None:
        all_elves.append([])
    else:
        all_elves[-1].append(int(line))
sums = []

for elf in all_elves:
    sums.append(sum(elf))

sums.sort()
print(sum(sums[-3:]))
