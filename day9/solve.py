import numpy as np

h = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [
        0,
        0,
        0,
        0,
        0,
    ],
    [0, 0, 0, 0, 0, 0],
    [
        0,
        0,
        0,
        0,
        0,
    ],
]
t = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [
        0,
        0,
        0,
        0,
        0,
    ],
    [0, 0, 0, 0, 0, 0],
    [
        0,
        0,
        0,
        0,
        0,
    ],
]


def move(vector, dir, step):
    if dir == "R":
        vector = [vector[0] + step, vector[1]]
    elif dir == "L":
        vector = [vector[0] - step, vector[1]]
    elif dir == "U":
        vector = [vector[0], vector[1] + step]
    elif dir == "D":
        vector = [vector[0], vector[1] - step]
    return vector


def get_newloc(vector2, vector1):

    x_dist = abs(vector1[0] - vector2[0])
    y_dist = abs(vector1[1] - vector2[1])

    if x_dist > 1 and y_dist >= 1:
        if vector1[0] > vector2[0]:
            dirx = -1
        else:
            dirx = 1

        if vector1[1] > vector2[1]:
            diry = -1
        else:
            diry = 1
        x_loc = vector1[0] + dirx
        y_loc = vector1[1] + diry
        # print("line 63")
        # print(vector2)
        # print(x_loc, y_loc)
        return [x_loc, y_loc]
    elif x_dist == 1 and y_dist > 1:
        if vector1[0] > vector2[0]:
            dirx = -1
        else:
            dirx = 1
        if vector1[1] > vector2[1]:
            diry = -1
        else:
            diry = 1
        x_loc = vector1[0] + dirx
        y_loc = vector1[1] + diry
        # print("line 68")
        # print(vector2)
        # print(x_loc, y_loc)
        return [x_loc, y_loc]
    elif x_dist > 1 and y_dist == 0:
        y_step = 0
        if vector2[0] - vector1[0] >= 1:
            x_step = 1
        else:
            x_step = -1
        x_loc = vector2[0] - x_step
        y_loc = vector2[1] - y_step
        # print("line 75")
        # print(vector2)
        # print(x_loc, y_loc)
        return [x_loc, y_loc]

    elif y_dist > 1 and x_dist == 0:
        x_step = 0
        if vector2[1] - vector1[1] >= 1:
            y_step = 1
        else:
            y_step = -1
        x_loc = vector1[0] + x_step
        y_loc = vector1[1] + y_step
        # print("line 83")
        # print(vector2)
        # print(x_loc, y_loc)
        return [x_loc, y_loc]

    else:
        return vector2


def get_far_dist(vector1, vector2):
    if abs(vector1[0] - vector2[0]) > 1 or abs(vector1[1] - vector2[1]) > 1:
        return True
    else:
        False


def draw_knots(vector_list):
    max_i = 0
    max_j = 0
    for knot in vector_list:
        if abs(knot[0]) > max_i:
            max_i = abs(knot[0])
        if abs(knot[1]) > max_j:
            max_j = abs(knot[1])
    max_i += 1
    max_j += 1
    ans = ""

    for j in [-max_j + j for j in range(2 * max_j)]:
        line_size = ["." for k in range(2 * max_i)]
        _line = "".join(line_size)
        _line = _line + "\n"
        for i in [-max_i + i for i in range(2 * max_i)]:
            if [i, j] in vector_list:
                if i >= 0:
                    index = max_i + i
                else:
                    index = -i
                if [i, j] == vector_list[0]:
                    char = "H"
                else:
                    char = "#"
                _line = _line[:index] + char + _line[index + 1 :]
        ans = _line + ans
    return ans


tail_locs = [[0, 0]]
vh = [0, 0]
vt = [0, 0]
f = open("tiny.txt", "r")
for line in f.readlines():
    _move = line.strip().split()
    steps = int(_move[1])
    for i in range(steps):
        new_vh = move(vh, _move[0], 1)
        if get_far_dist(new_vh, vt):
            vt = vh.copy()
        vh = new_vh
        if vt not in tail_locs:
            tail_locs.append(vt)

f.close()


tail_locs2 = [[0, 0]]

knots = [[0, 0] for i in range(10)]
f = open("input.txt", "r")
count = 0
for line in f.readlines():
    _move = line.strip().split()
    steps = int(_move[1])

    for j in range(steps):
        knots[0] = move(knots[0], _move[0], 1)

        for i in range(len(knots) - 1):
            if get_far_dist(knots[i], knots[i + 1]):
                print(f"now comparing {knots[i]} and {knots[i+1]}")
                knots[i + 1] = get_newloc(knots[i], knots[i + 1])

        # if count < 3:
        # print("1 Step Forward")
        # print(draw_knots(knots))
        # print(knots)
        if knots[9] not in tail_locs2:
            tail_locs2.append(knots[9])

    count += 1


f.close()

ans = draw_knots(knots)
print(ans)
f2 = open("draw.txt", "w")
f2.write(ans)
print(knots)
print(tail_locs2)
print(len(tail_locs2))

"4791"
"2352"
