import re

f = open("input.txt")
active_dir = ""
size_map = {}
dir_map = {}


def move_out(curr_dir):
    for i in range(len(curr_dir) - 1):
        char = curr_dir[-(i + 2)]
        if char == "/":
            return curr_dir[0 : -(i + 1)]


def find_parents(dir_name, size_map):
    output = []
    for candidate in size_map:
        if candidate != dir_name and candidate in dir_name:
            output.append(candidate)
    return output


for line in f.readlines():
    command = line.strip()

    if "$ cd" in command:
        if command == "$ cd ..":
            active_dir = move_out(active_dir)
        elif command == "$ cd /":
            active_dir = "/"
            size_map[active_dir] = 0
        else:
            active_dir = active_dir + command.split()[-1] + "/"
            size_map[active_dir] = 0

    if re.search("^\d{1,} ", command):
        size = command.split()[0]
        size_map[active_dir] += int(size)
        parents = find_parents(active_dir, size_map)
        for parent in parents:
            size_map[parent] += int(size)

total = 0
for dir_name in size_map:
    if size_map[dir_name] <= 100000:
        total += size_map[dir_name]

free_space = 70000000 - size_map["/"]

target_size = 30000000 - free_space
print(target_size)
candidate = "/"
candiate_size = size_map["/"]
for _dir in size_map:
    if size_map[_dir] >= target_size and size_map[_dir] < candiate_size:
        candidate = _dir
        candiate_size = size_map[_dir]
print(candiate_size)
