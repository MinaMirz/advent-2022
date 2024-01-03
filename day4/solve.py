f = open("input.txt", "r")
count = 0
for line in f.readlines():
    split_text = line.strip().split(",")
    ranges = [r.split("-") for r in split_text]
    ranges = [int(number) for r in ranges for number in r]
    if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or (
        ranges[0] <= ranges[2] and ranges[1] >= ranges[3]
    ):
        count += 1
print(count)

f2 = open("input.txt", "r")
count2 = 0
for line in f2.readlines():
    split_text = line.strip().split(",")
    ranges = [r.split("-") for r in split_text]
    ranges = [int(number) for r in ranges for number in r]

    if not ((ranges[1] < ranges[2]) or (ranges[3] < ranges[0])):
        count2 += 1

print(count2)
