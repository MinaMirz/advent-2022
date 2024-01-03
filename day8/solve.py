import numpy as np

f = open("input.txt", "r")
map = []
for line in f.readlines():
    l = line.strip()
    row = []
    for ch in l:
        i = int(ch)
        row.append(i)
    map.append(row)

arr = np.array(map)


def check_visible(x, y):
    X1 = arr[0:x, y]
    X2 = arr[x + 1 :, y]
    Y1 = arr[x, 0:y]
    Y2 = arr[x, y + 1 :]
    tree = arr[x, y]

    visibleX1 = True
    if X1.size > 0:
        if (X1 >= tree).any():
            visibleX1 = False

    visibleX2 = True
    if X2.size > 0:
        if (X2 >= tree).any():
            visibleX2 = False

    visibleY1 = True
    if Y1.size > 0:
        if (Y1 >= tree).any():
            visibleY1 = False

    visibleY2 = True
    if Y2.size > 0:
        if (Y2 >= tree).any():
            visibleY2 = False

    return visibleX1 or visibleX2 or visibleY1 or visibleY2


# numpy.vectorize(pyfunc)
count = 0
len_x, len_y = arr.shape
# check_visible(3, 5)

for i in range(len_x):
    for j in range(len_y):
        if check_visible(i, j):
            count += 1


def count_visible(x, y):
    X1 = arr[0:x, y]
    X1 = X1[::-1]
    X2 = arr[x + 1 :, y]
    Y1 = arr[x, 0:y]
    Y1 = Y1[::-1]
    Y2 = arr[x, y + 1 :]
    tree = arr[x, y]

    visibleX1 = 0
    if X1.size > 0:
        visibleX1 += 1
        for i, _tree in enumerate(X1):
            if _tree >= tree or i == len(X1) - 1:
                break
            visibleX1 += 1

    visibleX2 = 0
    if X2.size > 0:
        visibleX2 += 1
        for i, _tree in enumerate(X2):
            if _tree >= tree or i == len(X2) - 1:
                break
            visibleX2 += 1

    visibleY1 = 0
    if Y1.size > 0:
        visibleY1 += 1
        for i, _tree in enumerate(Y1):
            if _tree >= tree or i == len(Y1) - 1:
                break
            visibleY1 += 1

    visibleY2 = 0
    if Y2.size > 0:
        visibleY2 += 1
        for i, _tree in enumerate(Y2):
            if _tree >= tree or i == len(Y2) - 1:
                break
            visibleY2 += 1

    return visibleX1 * visibleX2 * visibleY1 * visibleY2


len_x, len_y = arr.shape
max = 0
I = None
J = None


for i in range(len_x):

    for j in range(len_y):
        cv = count_visible(i, j)

        if cv > max:
            max = cv
            I = i
            J = j


# print(count_visible(0, 2))
print(max, I, J)
# print(count_visible(2, 1))
# print(count_visible(1, 2))
"2261952"
"5762400"
"4709340"
"2395980"
"option 383520"
