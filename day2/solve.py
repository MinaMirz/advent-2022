file = open("input.txt", "r")


def calc_score(op, me):
    op = op.rstrip()
    me = me.rstrip()
    score = 0
    if me == "X":
        score += 1
        if op == "A":
            score += 3
        elif op == "B":
            score += 0
        elif op == "C":
            score += 6
        else:
            print("error")
            print(me, op)
    elif me == "Y":
        score += 2
        if op == "A":
            score += 6
        elif op == "B":
            score += 3
        elif op == "C":
            score += 0
        else:
            print("error")
            print(me, op)
    elif me == "Z":
        score += 3
        if op == "A":
            score += 0
        elif op == "B":
            score += 6
        elif op == "C":
            score += 3
        else:
            print("error")
            print(me, op)
    else:
        print("ERROR2")
        print(me, op)
    return score


sum = 0
count = 0
lines = file.readlines()
input_list = []

for line in lines:
    items = line.split()
    items[0] = items[0].rstrip()
    items[1] = items[1].rstrip()
    input_list.append(items)


for item in input_list:
    sum += calc_score(*item)

print(sum)


def calc_score2(op, result):
    op = op.rstrip()
    result = result.rstrip()
    score = 0
    if op == "A":
        if result == "X":
            score += 3
        elif result == "Y":
            score += 4
        elif result == "Z":
            score += 8
        else:
            print("error")
            print(op, result)
    elif op == "B":
        if result == "X":
            score += 1
        elif result == "Y":
            score += 5
        elif result == "Z":
            score += 9
        else:
            print("error")
            print(op, result)
    elif op == "C":
        if result == "X":
            score += 2
        elif result == "Y":
            score += 6
        elif result == "Z":
            score += 7
        else:
            print("error")
            print(op, result)
    else:
        print("ERROR2")
        print(op, result)
    return score


sum = 0
for item in input_list:
    sum += calc_score2(*item)

print(sum)
