f = open("tiny.txt")
job_que_obj = {"val": int, "runtime": int}
job_que = []
x = 1
check_points = [20, 60, 100, 140, 180, 220]
ans_list = []
cycle_count = 0
for line in f.readlines():
    # print(x)
    command = line.strip().split()

    if command[0] == "addx":

        cycle_count += 1
        if cycle_count in check_points:
            print("***- ", cycle_count * x)
            ans_list.append(cycle_count * x)
        cycle_count += 1
        if cycle_count in check_points:
            print("***- ", cycle_count * x)
            ans_list.append(cycle_count * x)
        x += int(command[1])

    else:
        cycle_count += 1
        if cycle_count in check_points:
            print("***- ", cycle_count * x)
            ans_list.append(cycle_count * x)
x = 1
f = open("input.txt")
ans = ""
cycle_count = 0
for line in f.readlines():
    # print(x)
    command = line.strip().split()

    if command[0] == "addx":

        cycle_count += 1
        if (cycle_count % 40) in [x, x + 1, x + 2]:
            ans = ans + "#"
        else:
            ans = ans + "."
        if cycle_count % 40 == 0:
            ans = ans + "\n"
        print(ans, x, cycle_count)
        cycle_count += 1
        if (cycle_count % 40) in [x, x + 1, x + 2]:
            ans = ans + "#"
        else:
            ans = ans + "."
        if cycle_count % 40 == 0:
            ans = ans + "\n"
        print(ans, x, cycle_count)
        x += int(command[1])

    else:
        cycle_count += 1
        if (cycle_count % 40) in [x, x + 1, x + 2]:
            ans = ans + "#"
        else:
            ans = ans + "."
        if cycle_count % 40 == 0:
            ans = ans + "\n"
        print(ans, x, cycle_count)


new_line = [40, 80, 120, 160, 200, 240]
print(ans)
