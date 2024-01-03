tiny = [1, 2, -3, 3, -2, 0, 4]


f = open("input.txt")
input = []
for line in f.readlines():
    input.append(int(line.strip("\n")))
# input = tiny


class ChainEl:
    def __init__(
        self,
        val,
        prev=None,
        next=None,
    ):
        self.val = val
        self.next = next
        self.prev = prev
        self.start = False

    def set_start(self, val=True):
        self.start = val
        return


def shift_forward(node):

    initial_node_ahead = node.next
    two_nodes_ahead = initial_node_ahead.next
    two_nodes_behind = node.prev
    initial_node_ahead.next = node
    initial_node_ahead.prev = two_nodes_behind

    node.prev = initial_node_ahead
    node.next = two_nodes_ahead

    two_nodes_ahead.prev = node
    two_nodes_behind.next = initial_node_ahead

    if node.start is True:
        node.set_start(False)
        node.prev.set_start(True)
    return


def shift_back(node):
    initial_node_behind = node.prev
    two_nodes_behind = initial_node_behind.prev
    two_nodes_ahead = node.next
    initial_node_behind.prev = node
    initial_node_behind.next = two_nodes_ahead

    node.next = initial_node_behind
    node.prev = two_nodes_behind

    two_nodes_behind.next = node
    two_nodes_ahead.prev = initial_node_behind

    if node.start is True:
        node.set_start(False)
        node.next.next.set_start(True)
    return


def find_start_node(node):
    start_node = node
    while start_node.start is not True:
        start_node = start_node.next
    return start_node


chain = None
start = None
ref = {}
for item in input:
    if chain is None:
        chain = ChainEl(item)
        chain.set_start()
        start = chain
        prev = chain
    else:
        chain = ChainEl(item, prev, None)
        prev.next = chain
        prev = chain
    ref[item] = chain

chain.next = start
start.prev = chain

chain = find_start_node(chain)
is_start = False
print("======first list=======")
while is_start is False:
    print(chain.val)
    chain = chain.next
    is_start = chain.start


"""
chain = find_start_node(chain)
# shift_back(chain.next.next)
shift_back(chain.prev.prev)
shift_back(chain.prev.prev.prev)
chain = find_start_node(chain)
is_start = False
print("======TEST=======")
while is_start is False:
    print(chain.val)
    chain = chain.next
    is_start = chain.start

"""

chain = find_start_node(chain)
print("======sorting list=======")
for key, node in ref.items():
    shift_step = node.val
    shift_abs = abs(shift_step)
    # print(shift_abs)
    for i in range(shift_abs):
        if shift_step > 0:
            shift_forward(node)
        if shift_step < 0:
            shift_back(node)

    print(node.prev.val, node.val, node.next.val)


chain = find_start_node(chain)
is_start = False
print("======decrypted list=======")
while is_start is False:
    print(chain.val)
    chain = chain.next
    is_start = chain.start


chain = find_start_node(chain)
while chain.val != 0:
    chain = chain.next

val1 = None
val2 = None
val3 = None
for i in range(3000):
    chain = chain.next
    if i == 999:
        val1 = chain.val
    if i == 1999:
        val2 = chain.val
    if i == 2999:
        val3 = chain.val

chain = find_start_node(chain)
is_start = False
count = 0
f2 = open("output.txt", "w")
while is_start is False:
    f2.write(f"{chain.val}\n")
    count += 1
    chain = chain.next
    is_start = chain.start
f2.close()
print(val1, val2, val3)
print(val1 + val2 + val3)
print(count)

"-17350"
"5962"
