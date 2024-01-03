import string


def get_priority(item):
    initial = string.ascii_lowercase.index(item.lower()) + 1
    if item.islower():
        return initial
    else:
        return initial + 26


Lines = open("input.txt").readlines()
sum = 0

for line in Lines:
    rucksack = line.strip()
    i = int(len(rucksack) / 2)
    r1 = rucksack[:i]
    r2 = rucksack[i:]
    for ch in r1:
        if ch in r2:
            sum += get_priority(ch)
            break

print(sum)

ans = []
i = 0
while i < len(Lines) - 1:
    l1 = Lines[i].strip()
    l2 = Lines[i + 1].strip()
    l3 = Lines[i + 2].strip()
    for ch in l1:
        if ch in l2:
            if ch in l3:
                ans.append(ch)
                break
    i += 3

sum = 0


for ch in ans:
    sum += get_priority(ch)


print(len(ans))
print(sum)
