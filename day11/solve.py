data_list = {
    0: {
        "Starting items": [{23: 79, 11: 79}, {23: 98, 11: 98}],
        "Operation": {"op_type": "a", "b": 19},
        "Test": {"test_type": "divisible", "val": 23, "If true": 2, "If false": 3},
    }
}
test_numbers = [23, 13, 17, 6, 2, 3, 7, 11, 19]
f = open("tiny.txt")
data = {}
for line in f.readlines():
    line = line.strip()
    if "Monkey" in line:
        new_monkey = line[-2]
        data[new_monkey] = {"count": 0}
    if "item" in line:
        _items = line.split(":")[-1].strip().split(", ")
        data[new_monkey]["items"] = []
        for item in _items:
            item_dic = {}
            for number in test_numbers:
                item_dic[number] = int(item) % number
            data[new_monkey]["items"].append(item_dic)

    if "Operation" in line:
        chunks = line.split()
        data[new_monkey]["Operation"] = {
            "a": chunks[-3],
            "op_type": chunks[-2],
            "b": chunks[-1],
        }

    if "Test" in line:
        chunks = line.split()
        data[new_monkey]["Test"] = {"val": int(chunks[-1])}
    if "true" in line:
        chunks = line.split()
        data[new_monkey]["Test"]["If true"] = chunks[-1]
    if "false" in line:
        chunks = line.split()
        data[new_monkey]["Test"]["If false"] = chunks[-1]


def perform_operation(old: int, op_dic: dict):

    if op_dic["a"] == "old":
        a = old
    else:
        a = int(op_dic["a"])
    if op_dic["b"] == "old":
        b = old
    else:
        b = int(op_dic["b"])
    if op_dic["op_type"] == "+":
        return a + b
    elif op_dic["op_type"] == "*":
        return a * b
    else:
        print("Error")
        return None


for i in range(20):
    for monkey in data:

        items = data[monkey]["items"].copy()
        del_index = []
        data[monkey]["count"] += len(items)
        for i, worry_levels in enumerate(items):
            for base, worry_level in worry_levels.items():
                new_worry_level = perform_operation(
                    worry_level, data[monkey]["Operation"]
                )
                worry_levels[base] = new_worry_level % base

            test_number = data[monkey]["Test"]["val"]
            if worry_levels[test_number] == 0:
                new_monkey = data[monkey]["Test"]["If true"]
            else:
                new_monkey = data[monkey]["Test"]["If false"]

            data[new_monkey]["items"].append(worry_levels)
            del_index.append(i)

        data[monkey]["items"] = []
        for i, number_dict in enumerate(items):
            if i not in del_index:
                data[monkey].append(number_dict)

monkey_business = 1
monkey_top = []

for monkey in data:
    print(f"Monkey {monkey} inspected {data[monkey]['count']} total items")
    if len(monkey_top) < 2:
        monkey_top.append(data[monkey]["count"])
    elif data[monkey]["count"] > monkey_top[0]:
        monkey_top.append(data[monkey]["count"])
        monkey_top.sort()
        monkey_top.pop(0)
    elif data[monkey]["count"] > monkey_top[1]:
        monkey_top.append(data[monkey]["count"])
        monkey_top.sort()
        monkey_top.pop(0)

monkey_business = monkey_top[0] * monkey_top[1]
print(monkey_top)
print(f"monkey business level is {monkey_business}")
