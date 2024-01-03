from statistics import median
from joblib import Parallel, delayed
import itertools


tunnel_map = {}
f = open("input.txt")
for line in f.readlines():
    specs = line.strip().split(";")
    valve_spec = specs[0].split()
    rout_detail = specs[1]

    valve_name = valve_spec[1]
    tunnel_map[valve_name] = {}

    flow_rate = int(valve_spec[4].split("=")[1])
    tunnel_map[valve_name]["flow_rate"] = flow_rate

    _routes = rout_detail.split()[4:]
    routes = []
    for route in _routes:
        route = route.strip(", ")
        routes.append(route)

    tunnel_map[valve_name]["routes"] = routes


def get_deadend_list(tunnel_map):
    dead_ends = []
    for node in tunnel_map:
        if len(tunnel_map[node]["routes"]) == 1:
            dead_end = [node]

            _node = tunnel_map[node]["routes"][0]
            dead_end.append(_node)
            options = len(tunnel_map[_node]["routes"])
            while options < 3:
                _nodes = tunnel_map[_node]["routes"]
                for item in _nodes:
                    if item not in dead_end:
                        _node = item
                        dead_end.append(_node)
                        options = len(tunnel_map[_node]["routes"])
            dead_end.pop()
            dead_ends.append(dead_end)
    return dead_ends


def count_open_valves(path):
    count = 0
    for item in path:
        if "open" in item:
            count += 1
    return count


def check_new_options(path, tunnel_map=tunnel_map):
    # check if this is an already finished path
    if path[-1] == "stop":
        return [path + ["stop"]]
    # check if all valves already open and stop moving
    if count_open_valves(path) == 15:
        return [path + ["stop"]]
    else:
        new_path_list = []
        if "open" in path[-1]:
            last_loc = path[-2]
            if "open" in path[-3]:
                second_to_last = path[-3].split("-")[0]
                #
            else:
                second_to_last = path[-3]

        else:
            last_loc = path[-1]
            if "open" in path[-2]:
                second_to_last = path[-2].split("-")[0]
                # print(f"second_to_last: {second_to_last}, in path: {path}")
            else:
                second_to_last = path[-2]
                # print(f"second_to_last: {second_to_last}, in path: {path}")

        new_branch_paths = []
        # print("new_actions before remove... ", tunnel_map[last_loc]["routes"])
        for item in tunnel_map[last_loc]["routes"]:
            if item == second_to_last and len(tunnel_map[last_loc]["routes"]) > 1:
                # print(f"remove last location {item}")
                continue
            if len(tunnel_map[item]["routes"]) == path.count(item):
                # print(f"{len(tunnel_map[item]['routes'])} and {path.count(item)}")
                # print(f"remove visited location {item}")
                continue
            new_branch_paths.append(item)
        # print("new_actions afer remove... ", new_branch_paths)
        if (f"{last_loc}-open" not in path) and (tunnel_map[last_loc]["flow_rate"] > 0):
            new_branch_paths = new_branch_paths + [f"{last_loc}-open"]
        if len(new_branch_paths) == 0:
            new_path_list = path + ["stop"]
            return [new_path_list]
        for new_action in new_branch_paths:
            new_path = path + [new_action]
            new_path_list.append(new_path)
        # print("new_actions afer open added... ", new_branch_paths)
        return new_path_list


def all_options(n, tunnel_map=tunnel_map):

    if n == 1:
        return [["AA"]]
    elif n == 2:
        new_actions = tunnel_map["AA"]["routes"]
        new_path_list = []
        for action in new_actions:
            new_path = ["AA", action]
            new_path_list.append(new_path)
        return new_path_list
    elif n > 2 and n < 10:

        existing_paths = all_options(n - 1)

        new_path_list = []
        for path in existing_paths:
            options = check_new_options(path)
            new_path_list = new_path_list + options

        print(f"step.. {n}")
        return new_path_list
    else:
        existing_paths = all_options(n - 1)
        outcomes = Parallel(n_jobs=8)(
            delayed(traverse_path)(path) for path in existing_paths
        )
        outcome_list_ = outcomes.copy()
        outcome_list_.sort()
        trunk = int(len(outcome_list_) / 3)
        bottom_vals = outcome_list_[0:trunk]
        new_path_list = []
        for i, val in enumerate(outcomes):
            if val not in bottom_vals:
                new_options = check_new_options(existing_paths[i])
                new_path_list = new_path_list + new_options
        print(f"step.. {n}")

        return new_path_list


def calc_pressure_release(open_valves, tunnel_map=tunnel_map):
    release = 0
    for valve in open_valves:
        release += tunnel_map[valve]["flow_rate"]
    return release


def traverse_path(path):
    open_valves = []
    released_pressure = 0
    for action in path:
        released_pressure += calc_pressure_release(open_valves)
        if "open" in action:
            valve_opened = action.split("-")[0]
            open_valves.append(valve_opened)
    return released_pressure


# print(tunnel_map)
# all_paths = all_options(31)


# outcome_list = Parallel(n_jobs=8)(delayed(traverse_path)(path) for path in all_paths)
# max_ = max(outcome_list)
# location_ = outcome_list.index(max_)
# print(max_)
# print(all_paths[location_])


def get_loc(step):
    if "open" in step:
        return step.split("-")[0]
    else:
        return step


def add_step(ans_dic, tunnel_map):
    path1 = ans_dic["path1"]
    path2 = ans_dic["path2"]
    last_step1 = get_loc(path1[-1])
    last_step2 = get_loc(path2[-1])
    total_flow = ans_dic["total_flow"]
    rate = ans_dic["total_flow_rate"]
    open_valves = ans_dic["open_list"]
    # check if this is an already finished path
    if last_step1 == "stop" and last_step2 == "stop":
        new_path1 = path1 + ["stop"]
        new_path2 = path2 + ["stop"]
        total = total_flow + rate
        return [
            {
                "path1": new_path1,
                "path2": new_path2,
                "open_list": open_valves,
                "total_flow": total,
                "total_flow_rate": rate,
            }
        ]
    # check if all valves already open and stop moving
    if len(open_valves) == 15:
        new_path1 = path1 + ["stop"]
        new_path2 = path2 + ["stop"]
        total = total_flow + rate
        return [
            {
                "path1": new_path1,
                "path2": new_path2,
                "open_list": open_valves,
                "total_flow": total,
                "total_flow_rate": rate,
            }
        ]
    else:
        new_branch_paths1 = []
        new_branch_paths2 = []

        second_to_last1 = get_loc(path1[-2])
        second_to_last2 = get_loc(path2[-2])

        if second_to_last1 == last_step1:
            second_to_last1 = get_loc(path1[-3])
        if second_to_last2 == last_step2:
            second_to_last2 = get_loc(path2[-3])

        if last_step1 != "stop":
            for item in tunnel_map[last_step1]["routes"]:
                if (
                    item == second_to_last1
                    and len(tunnel_map[last_step1]["routes"]) > 1
                ):
                    continue
                if len(tunnel_map[item]["routes"]) == path1.count(item):
                    continue
                new_branch_paths1.append(item)
            if (last_step1 not in open_valves) and (
                tunnel_map[last_step1]["flow_rate"] > 0
            ):
                new_branch_paths1 = new_branch_paths1 + [f"{last_step1}-open"]
        else:
            new_path1 = path1 + ["stop"]
        if last_step2 != "stop":
            for item in tunnel_map[last_step2]["routes"]:
                if (
                    item == second_to_last2
                    and len(tunnel_map[last_step2]["routes"]) > 1
                ):
                    continue
                if len(tunnel_map[item]["routes"]) == path2.count(item):
                    continue
                new_branch_paths2.append(item)
            if (last_step2 not in open_valves) and (
                tunnel_map[last_step2]["flow_rate"] > 0
            ):
                new_branch_paths2 = new_branch_paths2 + [f"{last_step2}-open"]
        else:
            new_path2 = path2 + ["stop"]

        if len(new_branch_paths1) == 0:
            new_branch_paths1 = ["stop"]

        if len(new_branch_paths2) == 0:
            new_branch_paths2 = ["stop"]

        new_ans_list = []
        for p1, p2 in itertools.product(new_branch_paths1, new_branch_paths2):
            if "open" in p1 and p1 == p2:
                continue
            new_path1 = path1 + [p1]
            new_path2 = path2 + [p2]
            new_open_valves = open_valves
            new_total = total_flow + rate
            new_rate = rate
            if "open" in p1:
                _valve = get_loc(p1)
                if _valve not in new_open_valves:
                    new_rate += tunnel_map[_valve]["flow_rate"]
                    new_open_valves = new_open_valves + [_valve]
            if "open" in p2:
                _valve = get_loc(p2)
                if _valve not in new_open_valves:
                    new_rate += tunnel_map[_valve]["flow_rate"]
                    new_open_valves = new_open_valves + [_valve]
            ans_dic = {
                "path1": new_path1,
                "path2": new_path2,
                "open_list": new_open_valves,
                "total_flow": new_total,
                "total_flow_rate": new_rate,
            }

            new_ans_list.append(ans_dic)
        return new_ans_list


def two_player(n, tunnel_map=tunnel_map):
    """
    return a list of three lists where:
    first list is each person's path.
    second list is their current total emisson
    third list is t

    """
    if n == 1:
        return [
            {
                "path1": ["AA"],
                "path2": ["AA"],
                "open_list": [],
                "total_flow": 0,
                "total_flow_rate": 0,
            }
        ]

    elif n == 2:

        new_actions = tunnel_map["AA"]["routes"]
        new_ans_list = []
        for a1, a2 in itertools.combinations(new_actions, 2):
            path1 = ["AA", a1]
            path2 = ["AA", a2]
            ans_dic = {
                "path1": path1,
                "path2": path2,
                "open_list": [],
                "total_flow": 0,
                "total_flow_rate": 0,
            }
            new_ans_list.append(ans_dic)
        print(f"step {n}")
        return new_ans_list

    elif n > 2 and n < 10:
        print(f"starting step {n}")
        previous_ans_list = two_player(n - 1)
        new_ans_list = []
        for ans_dic in previous_ans_list:
            new_ans_list = new_ans_list + add_step(ans_dic, tunnel_map)
        print(f"step {n}")
        return new_ans_list

    else:
        previous_ans_list = two_player(n - 1)
        """
         totals = []
        for ans_dic in previous_ans_list:
            totals.append(ans_dic["total_flow"])

        _threshold = median(totals) + (n / 5) ** 2
        new_ans_list = []
        for ans_dic in previous_ans_list:
            if ans_dic["total_flow"] > _threshold:
                new_ans_list = new_ans_list + add_step(ans_dic, tunnel_map)       
        
        """
        totals = []
        for _dic in previous_ans_list:
            totals.append(_dic["total_flow"])
        totals_s_ = totals.copy()
        totals_s_.sort()
        trunk = int(3 * len(totals_s_) / 4)
        bottom_vals = totals_s_[0:trunk]
        new_ans_list = []
        for i, val in enumerate(previous_ans_list):
            if val["total_flow"] not in bottom_vals:
                new_options = add_step(previous_ans_list[i], tunnel_map)
                new_ans_list = new_ans_list + new_options
        print(f"step {n}")
        return new_ans_list


all = two_player(27)

totals = []
for ans_dic in all:
    try:
        totals.append(ans_dic["total_flow"])
    except TypeError:
        print(ans_dic)
max_ = max(totals)
print(max_)
for ans_dic in all:
    if ans_dic["total_flow"] == max_:
        print(ans_dic["path1"])
        print(ans_dic["path2"])
        break
