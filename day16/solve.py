import random
from joblib import Parallel, delayed

tunnel_map = {"AA": {"flow_rate": 0, "routs": ["DD", "II", "BB"]}}
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


def calc_pressure_release(open_valves, tunnel_map):
    release = 0
    for valve in open_valves:
        release += tunnel_map[valve]["flow_rate"]
    return release


def build_weighted_action_list(valve, open_valves, tunnel_map):
    score_dic = {}
    for valve2 in tunnel_map[valve]["routes"]:
        if valve2 not in open_valves:
            score_dic[valve2] = 4
        else:
            score_dic[valve2] = 1
    if valve not in open_valves:
        score_dic["open"] = tunnel_map[valve]["flow_rate"]
    weighted_action_list = []
    for action, score in score_dic.items():
        _l = [action for i in range(score)]
        weighted_action_list = weighted_action_list + _l
    return weighted_action_list


def random_action(valve, open_valves, tunnel_map):
    action_list = build_weighted_action_list(valve, open_valves, tunnel_map)

    choice = random.choice(action_list)

    # print("open_valves ", open_valves)
    # print("valve ", valve)
    # print("action_list ", action_list)
    # print("choice", choice)
    return choice


def random_plan(iter):
    current_loc = "AA"
    open_valves = []
    released_pressure = 0
    for i in range(30):
        released_pressure += calc_pressure_release(open_valves, tunnel_map)
        decision = random_action(current_loc, open_valves, tunnel_map)
        if decision == "open":
            if current_loc not in open_valves:
                open_valves.append(current_loc)
        else:
            current_loc = decision
    # print("iteration ", iter)
    return released_pressure


outcome_list = Parallel(n_jobs=8)(delayed(random_plan)(i) for i in range(2 * 10**8))


print(max(outcome_list))

"1554"
"1602"
"1658"
"1679"
